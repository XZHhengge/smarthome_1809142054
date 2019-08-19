#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <errno.h>

extern int errno;

int main(int argc, char **argv)
{
    int    sockfd;
    struct sockaddr_in  servaddr;

    if (argc != 3)
        fprintf(stderr, "usage: cmd  <IP> <port>\n");

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        fprintf(stderr, "socket create error.\n");
        exit(1);
    }

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(atoi(argv[2]));
    if ( inet_pton(AF_INET, argv[1], &(servaddr.sin_addr)) < 0) {
        fprintf(stderr, "inet_pton error: %s\n", strerror(errno));
        close(sockfd);
        return -1;
    }

    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) != 0) {
        fprintf(stderr, "connect fail: %s\n", strerror(errno));
        exit(1);
    }

    int len = sizeof(struct sockaddr_in);
    char send[len + 1];

    memset(send, 0, len+1);
    memcpy(send, &servaddr, len);

     //unsigned char sin_len = servaddr.sin_len;
    unsigned short sa_family = servaddr.sin_family;
    unsigned short sin_port = servaddr.sin_port;
    unsigned int  s_addr = servaddr.sin_addr.s_addr;

    printf("%u %u %u\n", sa_family, sin_port, s_addr);
    int n=0;
    n = write(sockfd, send, len);
    if (n != len) {
        printf("write error\n");
    }

    printf("write over\n");
    exit(0);
}