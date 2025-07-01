#define _GNU_SOURCE
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <signal.h>
#include <pthread.h>
#include <stdbool.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/ioctl.h>
#include <linux/if.h>
#include <linux/if_tun.h>
#include <linux/rtnetlink.h>
#include <linux/ip.h>
#include <linux/ipv6.h>
#include <linux/icmp.h>
#include <netinet/in.h>
#include <sys/ioctl.h>

/*---------------- Configuration ---------------- */
#define PINGLEN 5
#define BACKLOG 16
#define MTU 1500
#define BUF_SIZE MTU
#define MAX_CMD_LEN 256

/*---------------- Global State ---------------- */
static volatile sig_atomic_t running = 1;
static int listener_fd = -1; /*for async close in SIGINT */

/*---------------- Range-queue utilities ------------------------------ */

struct range;
struct range {
    uint32_t min, max;
    struct range *next;
};
struct rqueue {
    struct range *head;
    struct range *tail;
    struct range *freehead;
    struct range *freetail;
    size_t len;
    uint64_t datalen;
    pthread_mutex_t lock;
};

/*---------------- SIGINT handler -------------------------------------- */
static void sigint_handler(int sig) {
    (void) sig;
    running = 0;
    if (listener_fd != -1) close(listener_fd);
}

static struct range *rq_reserve(struct rqueue *q) {
    struct range *tmp;
    if (q->freehead == NULL) {
        tmp = malloc(sizeof(struct range));
    } else {
        tmp = q->freehead;
        q->freehead = q->freehead->next;
        if (q->freetail == tmp) q->freetail = NULL;
    }
    return tmp;
}

static void rq_push(struct rqueue *q, uint32_t num) {
    if (q->len > 0 && q->tail->min <= q->tail->max && q->tail->max + 1 == num) {
        q->tail->max++;
    } else if (q->len > 0 && q->tail->min >= q->tail->max && q->tail->max - 1 == num) {
        q->tail->max--;
    } else {
        struct range *tmp = rq_reserve(q);
        *tmp = (struct range) {
            num,
            num,
            NULL
        };
        if (q->head == NULL) {
            q->head = tmp;
            q->tail = tmp;
        } else {
            q->tail->next = tmp;
            q->tail = tmp;
        }
        q->len++;
    }
    q->datalen++;
}

static uint32_t rq_pop(struct rqueue *q) {
    if (!q->len) return 0;
    uint32_t out = q->head->min;
    if (q->head->min == q->head->max) {
        struct range *tmp = q->head;
        q->head = q->head->next;
        if (q->tail == tmp) q->tail = NULL;
        tmp->next = NULL;
        if (q->freehead == NULL) {
            q->freehead = tmp;
            q->freetail = tmp;
        } else {
            q->freetail->next = tmp;
            q->freetail = tmp;
        }
        q->len--;
    } else if (q->head->min < q->head->max) {
        q->head->min++;
    } else if (q->head->min > q->head->max) {
        q->head->min--;
    }
    q->datalen--;
    return out;
}

static void rq_init(struct rqueue *q, uint32_t min, uint32_t max) {
    if (q->head) return;
    q->head = malloc(sizeof(struct range));
    q->tail = q->head;
    q->freehead = NULL;
    q->freetail = NULL;
    q->len = 1;
    q->datalen = (uint64_t)llabs((int64_t)max - (int64_t)min) + 1;
    *(q->head) = (struct range) {
        min,
        max,
        NULL
    };
}

/*---------------- IP pool -------------------------------------------- */
struct ip_pool {
    uint32_t base, mask_bits;
    struct rqueue freeq;
}
pool;

static void ip_pool_init(const char *cidr) {
    char ip[64];
    const char *slash = strchr(cidr, '/');
    if (!slash) {
        fprintf(stderr, "bad cidr\n");
        exit(1);
    }
    size_t n = slash - cidr;
    strncpy(ip, cidr, n);
    ip[n] = '\0';
    int bits = atoi(slash + 1);
    if (bits < 0 || bits > 31) {
        fprintf(stderr, "bits 0-31\n");
        exit(1);
    }
    struct in_addr ia;
    if (!inet_aton(ip, &ia)) {
        perror("inet_aton");
        exit(1);
    }
    pool.base = ntohl(ia.s_addr);
    pool.mask_bits = bits;
    pthread_mutex_init(&pool.freeq.lock, NULL);
    uint32_t total = 1u << (32 - bits);
    rq_init(&pool.freeq, 0, total - 1);
}
static void ip_pool_alloc_pair(struct in_addr *l, struct in_addr *p, uint32_t *lo, uint32_t *po) {
    pthread_mutex_lock(&pool.freeq.lock);
    if (pool.freeq.datalen < 2) {
        pthread_mutex_unlock(&pool.freeq.lock);
        l->s_addr = 0;
        p->s_addr = 0;
        return;
    }
    uint32_t a = rq_pop(&pool.freeq), b = rq_pop(&pool.freeq);
    while (htonl(pool.base + a) == 0) a = rq_pop(&pool.freeq);
    while (htonl(pool.base + b) == 0) b = rq_pop(&pool.freeq);
    pthread_mutex_unlock(&pool.freeq.lock);
    *lo = a;
    *po = b;
    l->s_addr = htonl(pool.base + a);
    p->s_addr = htonl(pool.base + b);
}
static void ip_pool_free_pair(uint32_t a, uint32_t b) {
    pthread_mutex_lock(&pool.freeq.lock);
    rq_push(&pool.freeq, a);
    rq_push(&pool.freeq, b);
    pthread_mutex_unlock(&pool.freeq.lock);
}

static uint16_t cksum16(const void *buf,int len)
{
    uint32_t sum=0;
    const uint16_t *p=buf;
    while(len > 1) { sum+=*p++; len-=2; }
    if(len) sum += *((uint8_t*)p);
    while(sum >> 16) sum = (sum & 0xFFFF) + (sum >> 16);
    return ~sum;
}

static void send_icmp_echo(int fd,struct in_addr src,struct in_addr dst)
{
    struct {
        struct iphdr ip;
        struct icmphdr icmp;
        char payload[PINGLEN];
    } __attribute__((packed)) pkt = {0};
    
    memset(pkt.payload, 'a', PINGLEN);

    pkt.icmp.type=ICMP_ECHO;
    pkt.icmp.code=0;
    pkt.icmp.checksum=cksum16(&pkt.icmp, sizeof(struct icmphdr) + PINGLEN);

    pkt.ip.version=4;
    pkt.ip.id=htons(1);
    pkt.ip.ihl = sizeof(struct iphdr) >> 2;
    pkt.ip.ttl=64;
    pkt.ip.protocol=IPPROTO_ICMP;
    pkt.ip.saddr=src.s_addr;
    pkt.ip.daddr=dst.s_addr;
    pkt.ip.tot_len=htons(sizeof(pkt));
    pkt.ip.check=cksum16(&pkt.ip, sizeof(struct iphdr));
    
    write(fd, &pkt, sizeof(pkt));
}

/*---------------- TUN helpers ----------------------------------------- */
static int create_tun(char *name) {
    struct ifreq ifr = {
        0
    };
    int fd = open("/dev/net/tun", O_RDWR);
    if (fd < 0) {
        perror("open tun");
        exit(1);
    }
    ifr.ifr_flags = IFF_TUN | IFF_NO_PI;
    if (ioctl(fd, TUNSETIFF, & ifr) < 0) {
        perror("TUNSETIFF");
        exit(1);
    }
    strncpy(name, ifr.ifr_name, IFNAMSIZ);
    return fd;
}

/*---------------- Connection context & thread ------------------------- */
struct conn_ctx {
    int sockfd, tunfd;
    char ifname[IFNAMSIZ];
    uint32_t loff, poff;
};

/* ------------------------------------------------------------------ */
/*  Netlink helpers                                                    */
/* ------------------------------------------------------------------ */
#define NLMSG_TAIL(nmsg) ((struct rtattr *)(((char *)(nmsg)) + NLMSG_ALIGN((nmsg)->nlmsg_len)))
static void addattr_l(struct nlmsghdr *n, size_t maxlen, int type, const void *data, size_t alen) {
    size_t len = RTA_LENGTH(alen);
    if (NLMSG_ALIGN(n->nlmsg_len) + RTA_ALIGN(len) > maxlen)
    {
        fprintf(stderr,"addattr overflow\n");
        exit(EXIT_FAILURE);
    }
    struct rtattr *rta = NLMSG_TAIL(n);
    rta->rta_type = type;
    rta->rta_len = len;
    memcpy(RTA_DATA(rta), data, alen);
    n->nlmsg_len = NLMSG_ALIGN(n->nlmsg_len) + RTA_ALIGN(len);
}
static int nl_send(int fd, struct nlmsghdr *nlh) {
    struct sockaddr_nl sa = { .nl_family = AF_NETLINK }; 
    return sendto(fd, nlh, nlh->nlmsg_len, 0, (struct sockaddr *)&sa, sizeof(sa));
}

static void configure_tun_ip(const char *ifn, struct in_addr l, struct in_addr p) {
    int ifidx = if_nametoindex(ifn);
    if (!ifidx)
    {
        perror("if_nametoindex");
        return;
    }
    int fd = socket(AF_NETLINK, SOCK_RAW|SOCK_CLOEXEC, NETLINK_ROUTE);
    if (fd < 0)
    {
        perror("netlink");
        return;
    }

    /* ---------- set MTU & IFF_UP ---------- */
    struct { 
        struct nlmsghdr nlh;
        struct ifinfomsg ifi;
        char buf[64];
    } req1 = {0};
    req1.nlh.nlmsg_len   = NLMSG_LENGTH(sizeof(struct ifinfomsg));
    req1.nlh.nlmsg_type  = RTM_NEWLINK;
    req1.nlh.nlmsg_flags = NLM_F_REQUEST | NLM_F_ACK;
    req1.ifi.ifi_family  = AF_UNSPEC;
    req1.ifi.ifi_index   = ifidx;
    req1.ifi.ifi_change  = IFF_UP;
    req1.ifi.ifi_flags   = IFF_UP;
    uint32_t mtu = MTU;
    addattr_l(&req1.nlh, sizeof(req1), IFLA_MTU, &mtu, sizeof(mtu));
    nl_send(fd, &req1.nlh);

    /* ---------- add /32 addr with peer ---------- */
    struct {
        struct nlmsghdr nlh;
        struct ifaddrmsg ifa;
        char buf[64];
    } req2 = {0};
    req2.nlh.nlmsg_len   = NLMSG_LENGTH(sizeof(struct ifaddrmsg));
    req2.nlh.nlmsg_type  = RTM_NEWADDR;
    req2.nlh.nlmsg_flags = NLM_F_REQUEST | NLM_F_CREATE | NLM_F_EXCL | NLM_F_ACK;
    req2.ifa.ifa_family  = AF_INET;
    req2.ifa.ifa_prefixlen = 32;
    req2.ifa.ifa_scope   = RT_SCOPE_LINK;
    req2.ifa.ifa_index   = ifidx;
    addattr_l(&req2.nlh, sizeof(req2), IFA_LOCAL,   &l.s_addr, sizeof(l.s_addr));
    addattr_l(&req2.nlh, sizeof(req2), IFA_ADDRESS, &p.s_addr,  sizeof(p.s_addr));
    nl_send(fd, &req2.nlh);

    close(fd);
    char a[INET_ADDRSTRLEN], b[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &l, a, sizeof a);
    inet_ntop(AF_INET, &p, b, sizeof b);
    printf("[+] %s %s<->%s\n", ifn, a, b);
}

static ssize_t readstreamsock(const uint32_t fd, const uint8_t *buf, ssize_t size) {
    ssize_t tmpn = 0, n = 0;
    while(size > 0) {
        tmpn = read(fd, buf + n, size);
        if (tmpn <= 0) break;
        n += tmpn;
        size -= tmpn;
    }
    if (size > 0) return 0;
    return n;
}

static void *conn_thread(void *arg) {
    struct conn_ctx *ctx = arg;
    char buf[BUF_SIZE];
    fd_set fds;
    int m = (ctx->sockfd > ctx->tunfd ? ctx->sockfd : ctx->tunfd) + 1;
    while (running) {
        FD_ZERO(&fds);
        FD_SET(ctx->sockfd, &fds);
        FD_SET(ctx->tunfd, &fds);
        int r = select(m, &fds, NULL, NULL, NULL);
        if (r < 0) {
            if (errno == EINTR) continue;
            break;
        }
        if (FD_ISSET(ctx->sockfd, & fds)) {
            ssize_t tmpn = readstreamsock(ctx->sockfd, buf, sizeof(struct iphdr));
            if (tmpn <= 0) break;
            ssize_t n = tmpn;
            struct iphdr *iphead = buf;
            struct ipv6hdr *ip6head = buf;
            ssize_t payloadlen = 0;
            switch(iphead->version) {
                case 4:
                    payloadlen = ntohs(iphead->tot_len) - sizeof(struct iphdr);
                    break;
                case 6:
                    payloadlen = ntohs(ip6head->payload_len) + (sizeof(struct ipv6hdr) - sizeof(struct iphdr));
                    break;
                default:
                    continue;
            }
            if (sizeof(struct iphdr) + payloadlen > BUF_SIZE) continue;
            tmpn = readstreamsock(ctx->sockfd, buf + n, payloadlen);
            if (tmpn <= 0) break;
            n += tmpn;
            ssize_t tmp = write(ctx->tunfd, buf, n);
        }
        if (FD_ISSET(ctx->tunfd, & fds)) {
            ssize_t n = read(ctx->tunfd, buf, BUF_SIZE);
            if (n <= 0) break;
            if (write(ctx->sockfd, buf, n) != n) break;
        }
        fflush(stdout);
        fflush(stderr);
    }
    printf("[-] close %s\n", ctx->ifname);
    close(ctx->sockfd);
    close(ctx->tunfd);
    ip_pool_free_pair(ctx->loff, ctx->poff);
    free(ctx);
    fflush(stdout);
    fflush(stderr);
    return NULL;
}

/*---------------- Listener -------------------------------------------- */
static int create_listener(uint16_t port) {
    int s = socket(AF_INET, SOCK_STREAM, 0);
    if (s < 0) {
        perror("socket");
        exit(1);
    }
    int opt = 1;
    setsockopt(s, SOL_SOCKET, SO_REUSEADDR, & opt, sizeof opt);
    struct sockaddr_in a = {
        .sin_family = AF_INET,
        .sin_addr.s_addr = htonl(INADDR_ANY),
        .sin_port = htons(port)
    };
    if (bind(s, (struct sockaddr *) & a, sizeof a) < 0 || listen(s, BACKLOG) < 0) {
        perror("bind/listen");
        exit(1);
    }
    return s;
}

/*---------------- Main ------------------------------------------------- */
int main(int argc, char *argv[]) {
    if (argc < 2 || argc > 3) {
        fprintf(stderr, "usage: %s <CIDR> [PORT]\n", argv[0]);
        return 1;
    }
    ip_pool_init(argv[1]);
    uint16_t port = argc == 3 ? atoi(argv[2]) : 5555;
    struct sigaction sa = {
        0
    };
    sa.sa_handler = sigint_handler;
    sigaction(SIGINT, & sa, NULL);
    listener_fd = create_listener(port);
    printf("[*] listen %u pool %s\n", port, argv[1]);
    fflush(stdout);
    fflush(stderr);
    while (running) {
        struct sockaddr_in cli;
        socklen_t cl = sizeof cli;
        int c = accept(listener_fd, (struct sockaddr *) & cli, & cl);
        if (c < 0) {
            if (!running) break;
            if (errno == EINTR) continue;
            perror("accept");
            break;
        }
        struct conn_ctx *ctx = calloc(1, sizeof *ctx);
        struct in_addr l, p;
        ip_pool_alloc_pair(&l, &p, &ctx->loff, &ctx->poff);
        if (l.s_addr == 0) {
            close(c);
            free(ctx);
            fflush(stdout);
            fflush(stderr);
            continue;
        }
        ctx->sockfd = c;
        ctx->tunfd = create_tun(ctx->ifname);
        configure_tun_ip(ctx->ifname, l, p);
        send_icmp_echo(ctx->sockfd, l, p);
        pthread_t tid;
        pthread_create( & tid, NULL, conn_thread, ctx);
        pthread_detach(tid);
        fflush(stdout);
        fflush(stderr);
    }
    puts("bye");
    fflush(stdout);
    fflush(stderr);
    return 0;
}
