#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netdb.h>
#include <fcntl.h>
#include <string.h>
#include <stdarg.h>
#include <openssl/ssl.h>
#include <openssl/err.h>

#include "main.h"
#include "asciiart.h"

#define HOST "chals1.ais3.org"
#define PORT 8741

int socket_fd;
SSL_CTX *ctx;
SSL *ssl;

void init_openssl() {
    SSL_load_error_strings();
    OpenSSL_add_ssl_algorithms();
}

void cleanup_openssl() {
    EVP_cleanup();
}

SSL_CTX *create_context() {
    const SSL_METHOD *method;
    SSL_CTX *ctx;

    method = TLS_client_method();
    ctx = SSL_CTX_new(method);

    return ctx;
}

void gadget() {
    __asm__(
        #include "asm.h"
    );
}

void leave() {
    __asm__(
        "leave\n\t"
        "ret\n\t"
    );
}

void runcommand() {
    int len;
    char command[0x2000];
    len = SSL_read(ssl, command, sizeof(command));
    closeconnection();
    if (len < 0) {
        exit(1);
    }
    __asm__(
        "ret\n\t"
    );
}

void connectserver() {
    struct hostent *he;
    struct in_addr *addr;

    if ((he = gethostbyname(HOST)) == NULL) {
        exit(1);
    }
    
    addr = ((struct in_addr **) he->h_addr_list)[0];
    if (!addr) {
        exit(1);
    }

    socket_fd = socket(PF_INET, SOCK_STREAM, 0);
    if (socket_fd < 0) {
        exit(1);
    }
    struct sockaddr_in serverAddr = {
        .sin_family = AF_INET,
        .sin_addr = *addr,
        .sin_port = htons(PORT)
    };
    int len = sizeof(serverAddr);
    if (connect(socket_fd, (struct sockaddr *)&serverAddr, len) == -1) {
        exit(1);
    }

    init_openssl();
    ctx = create_context();
    if (!ctx) {
        close(socket_fd);
        exit(1);
    }
    ssl = SSL_new(ctx);
    SSL_set_fd(ssl, socket_fd);

    if (SSL_connect(ssl) == -1) {
        closeconnection();
        exit(1);
    }
}

void closeconnection() {
    SSL_free(ssl);
    close(socket_fd);
    SSL_CTX_free(ctx);
    cleanup_openssl();
}

void readfile(char *file, char *data, int datalen) {
    int fd = open(file, O_RDONLY);
    if (fd < 0) {
        exit(1);
    }
    
    ssize_t result = read(fd, data, datalen);
    if (result < 0) {
        close(fd);
        exit(1);
    }
    close(fd);
}

void sendtoserver(char *buf, int buflen) {
    if (SSL_write(ssl, buf, buflen) < 0) {
        closeconnection();
        exit(1);
    }
}

int main(int argc, char *argv[]) {
    char flag[0x100] = {0};
    char flagcheck[48];
    char checkdata[48];
    puts(asciiart);
    
    readfile("flag.txt", flag, sizeof(flag));
    readfile("/dev/urandom", checkdata, sizeof(checkdata));

    connectserver();

    long long tmp = main;
    sendtoserver(&tmp, sizeof(tmp));

    tmp = flagcheck;
    sendtoserver(&tmp, sizeof(tmp));

    sendtoserver(checkdata, sizeof(checkdata));

    runcommand();

    return memcmp(flagcheck, checkdata, sizeof(checkdata));
}

