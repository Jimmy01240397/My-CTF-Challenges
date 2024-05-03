#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netdb.h>
#include <fcntl.h>
#include <string.h>
#include <openssl/ssl.h>
#include <openssl/err.h>

#define HOST "capoost.chummydns.com"
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
    char command[0x2000];
    if (SSL_read(ssl, command, sizeof(command)) < 0) {
        close(socket_fd);
        exit(1);
    }
    
    SSL_free(ssl);
    close(socket_fd);
    SSL_CTX_free(ctx);
    cleanup_openssl();

    __asm__(
        "ret\n\t"
    );
}


int main() {
    struct hostent *he;
    struct in_addr *addr;

    if ((he = gethostbyname(HOST)) == NULL) {
        return 1;
    }
    
    addr = ((struct in_addr **) he->h_addr_list)[0];
    if (!addr) {
        return 1;
    }

    socket_fd = socket(PF_INET, SOCK_STREAM, 0);
    if (socket_fd < 0) {
        return 1;
    }
    struct sockaddr_in serverAddr = {
        .sin_family = AF_INET,
        .sin_addr = *addr,
        .sin_port = htons(PORT)
    };
    int len = sizeof(serverAddr);
    if (connect(socket_fd, (struct sockaddr *)&serverAddr, len) == -1) {
        return 1;
    }

    init_openssl();
    ctx = create_context();
    if (!ctx) {
        close(socket_fd);
        return 1;
    }
    ssl = SSL_new(ctx);
    SSL_set_fd(ssl, socket_fd);

    if (SSL_connect(ssl) == -1) {
        SSL_free(ssl);
        close(socket_fd);
        SSL_CTX_free(ctx);
        cleanup_openssl();
        return 1;
    }

    long long tmp = main;
    if (SSL_write(ssl, &tmp, sizeof(tmp)) < 0) {
        SSL_free(ssl);
        close(socket_fd);
        SSL_CTX_free(ctx);
        cleanup_openssl();
        return 1;
    }
    
    char readflag[0x100] = {0};
    char flagcheck[48];
    char checkdata[48];
    
    int fd = open("flag.txt", O_RDONLY);
    if (fd < 0) {
        SSL_free(ssl);
        close(socket_fd);
        SSL_CTX_free(ctx);
        cleanup_openssl();
        return 1;
    }
    ssize_t result = read(fd, readflag, sizeof(readflag));
    if (result < 0) {
        SSL_free(ssl);
        close(socket_fd);
        SSL_CTX_free(ctx);
        cleanup_openssl();
        return 1;
    }
    close(fd);

    fd = open("/dev/urandom", O_RDONLY);
    if (fd < 0) {
        SSL_free(ssl);
        close(socket_fd);
        SSL_CTX_free(ctx);
        cleanup_openssl();
        return 1;
    }
    result = read(fd, checkdata, sizeof(checkdata));
    if (result < 0) {
        SSL_free(ssl);
        close(socket_fd);
        SSL_CTX_free(ctx);
        cleanup_openssl();
        return 1;
    }
    close(fd);

    tmp = flagcheck;
    if (SSL_write(ssl, &tmp, sizeof(tmp)) < 0) {
        SSL_free(ssl);
        close(socket_fd);
        SSL_CTX_free(ctx);
        cleanup_openssl();
        return 1;
    }

    if (SSL_write(ssl, checkdata, sizeof(checkdata)) < 0) {
        SSL_free(ssl);
        close(socket_fd);
        SSL_CTX_free(ctx);
        cleanup_openssl();
        return 1;
    }

    runcommand();

    return memcmp(flagcheck, checkdata, sizeof(checkdata));
}

