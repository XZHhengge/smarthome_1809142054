
/*client.c*/

#include <time.h>
#include <sys/time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <strings.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> /* netbd.h is needed for struct hostent =) */

#define PORT 23333 /* Open Port on Remote Host */
#define MAXDATASIZE 100 /* Max number of bytes of data */

/*
 udp广播通信，执行时需要两个参数如下：
 ./client 192.168.1.255
 这样便会对192.168.1这个网段内所有开着./server的主机发送数据
 */
//int main(int argc, char *argv[])
int main(int argc, char *argv[])
{

    int fd, numbytes; /* files descriptors */
    char recvbuf[MAXDATASIZE]; /* buf will store received text */
    char sendbuf[MAXDATASIZE];
    struct hostent *he; /* structure that will get information about remote host */
    struct sockaddr_in server,client; /* server's address information */
    int yes;

    /* this is used because our program will need two argument (IP address and a message */

    if (argc !=2) {
        printf("Usage: %s <IP Address> \n",argv[0]);
        exit(1);
    }

    if ((he=gethostbyname(argv[1]))==NULL){ // calls gethostbyname()
        printf("gethostbyname() error\n");
        exit(1);
    }


    if ((fd=socket(AF_INET, SOCK_DGRAM, 0))==-1){ // calls socket()
        printf("socket() error\n");
        exit(1);
    }

    /* 设置通讯方式对广播，即本程序发送的一个消息，网络上所有主机均可以收到 */
    yes = 1;
    setsockopt(fd, SOL_SOCKET, SO_BROADCAST, &yes, sizeof(yes));

    bzero(&server,sizeof(server));
    server.sin_family = AF_INET;
    server.sin_port = htons(PORT); /* htons() is needed again */
    server.sin_addr = *((struct in_addr *)he->h_addr); /*he->h_addr passes "*he"'s info to "h_addr" */

    socklen_t len;
    len=sizeof(struct sockaddr_in);
    while (1) {
        printf("input message:");
        fgets(sendbuf,40,stdin);

//        struct Books
//        {
//            unsigned short id;
//
//            char tag;
//
//            unsigned int version;
//
//            unsigned int count;
//        }book = {123, (char) "zz", 12334, 123456}
//        ;
//        sendto(fd,sendbuf,strlen(sendbuf),0,(struct sockaddr *)&server,len);
//         心跳包: 设备号,状态,类型,
        char[20] book = '123413131'
        sendto(fd, (char*)&book, sizeof(book)+1,0,(struct sockaddr *)&server,len);
        numbytes=recvfrom(fd,recvbuf,MAXDATASIZE,0,(struct sockaddr *)&server,&len);
        if (numbytes == -1){ /* calls recvfrom() */
            printf("recvfrom() error\n");
            exit(1);
        }
        if(numbytes>0){
            printf("recvfrom Message:%s", recvbuf);
        }
        recvbuf[numbytes]='\0';


    }

    close(fd); /* close fd */
}