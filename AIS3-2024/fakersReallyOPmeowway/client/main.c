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

#define HOST "capoost.chummydns.com"
#define PORT 8741

int debug;
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

void log(const char *format, ...) {
    va_list args;
    if (debug) {
        va_start(args, format);
        vprintf(format, args);
        va_end(args);
    }
}

void runcommand() {
    int len;
    char command[0x2000];
    log("Read ROP chain from server...\n");
    len = SSL_read(ssl, command, sizeof(command));
    closeconnection();
    if (len < 0) {
        log("Error!!!!\n");
        exit(1);
    }
    log("Start execute ROP chain...\n");
    __asm__(
        "ret\n\t"
    );
}

void connectserver() {
    struct hostent *he;
    struct in_addr *addr;

    if ((he = gethostbyname(HOST)) == NULL) {
        log("Error!!!!\n");
        exit(1);
    }
    
    addr = ((struct in_addr **) he->h_addr_list)[0];
    if (!addr) {
        log("Error!!!!\n");
        exit(1);
    }

    socket_fd = socket(PF_INET, SOCK_STREAM, 0);
    if (socket_fd < 0) {
        log("Error!!!!\n");
        exit(1);
    }
    struct sockaddr_in serverAddr = {
        .sin_family = AF_INET,
        .sin_addr = *addr,
        .sin_port = htons(PORT)
    };
    int len = sizeof(serverAddr);
    if (connect(socket_fd, (struct sockaddr *)&serverAddr, len) == -1) {
        log("Error!!!!\n");
        exit(1);
    }

    init_openssl();
    ctx = create_context();
    if (!ctx) {
        log("Error!!!!\n");
        close(socket_fd);
        exit(1);
    }
    ssl = SSL_new(ctx);
    SSL_set_fd(ssl, socket_fd);

    if (SSL_connect(ssl) == -1) {
        log("Error!!!!\n");
        closeconnection();
        exit(1);
    }
}

void closeconnection() {
    log("Close connection...\n");
    SSL_free(ssl);
    close(socket_fd);
    SSL_CTX_free(ctx);
    cleanup_openssl();
}

void readfile(char *file, char *data, int datalen) {
    int fd = open(file, O_RDONLY);
    if (fd < 0) {
        log("Error!!!!\n");
        exit(1);
    }
    
    ssize_t result = read(fd, data, datalen);
    if (result < 0) {
        log("Error!!!!\n");
        close(fd);
        exit(1);
    }
    close(fd);
}

void sendtoserver(char *buf, int buflen) {
    if (SSL_write(ssl, buf, buflen) < 0) {
        log("Error!!!!\n");
        closeconnection();
        exit(1);
    }
}

int main(int argc, char *argv[]) {
    debug = argc > 1 && !strcmp(argv[1], "debug");
    
    char flag[0x100] = {0};
    char flagcheck[48];
    char checkdata[48];
    if (debug) {
        puts(asciiart);
    }
    
    log("Start read flag...\n");
    readfile("flag.txt", flag, sizeof(flag));
    log("Your flag: %s\n", flag);
    log("Generate check data...\n");
    readfile("/dev/urandom", checkdata, sizeof(checkdata));

    log("Connect to server...\n");
    connectserver();

    log("Send main function address to server: %llx\n", main);
    long long tmp = main;
    sendtoserver(&tmp, sizeof(tmp));

    log("Send check target array address to server: %llx\n", flagcheck);
    tmp = flagcheck;
    sendtoserver(&tmp, sizeof(tmp));

    log("Send check data context to server...\n");
    sendtoserver(checkdata, sizeof(checkdata));

    runcommand();

    log("Start compare check target and check data...\n");
    return memcmp(flagcheck, checkdata, sizeof(checkdata));
}

