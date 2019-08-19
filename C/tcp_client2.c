#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define SERVER_PORT 5555

/*
 连接到服务器后，会不停循环，等待输入，
 输入quit后，断开与服务器的连接
 */

int main()
{
    //获取当前时间
//    time_t tmpcal_ptr;
//	struct tm *tmp_ptr = NULL;
//
//	tmp_ptr = localtime(&tmpcal_ptr);
//	printf ("after localtime, the time is:%d.%d.%d ", (1900+tmp_ptr->tm_year), (1+tmp_ptr->tm_mon), tmp_ptr->tm_mday);
//	printf("%d:%d:%d\n", tmp_ptr->tm_hour, tmp_ptr->tm_min, tmp_ptr->tm_sec);

    //客户端只需要一个套接字文件描述符，用于和服务器通信
	int clientSocket;
    //描述服务器的socket
	struct sockaddr_in serverAddr;
	char sendbuf[200];
	char recvbuf[200];
	int iDataNum;
	if((clientSocket = socket(AF_INET, SOCK_STREAM, 0)) < 0)
	{
		perror("socket");
		return 1;
	}

	serverAddr.sin_family = AF_INET;
	serverAddr.sin_port = htons(SERVER_PORT);
    //指定服务器端的ip，本地测试：127.0.0.1
    //inet_addr()函数，将点分十进制IP转换成网络字节序IP
	serverAddr.sin_addr.s_addr = inet_addr("94.191.87.62");
//	serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	if(connect(clientSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) < 0)
	{
		perror("connect");
		return 1;
	}


	while(1)
	{
//		printf("Input your world:>");
//		scanf("%s", sendbuf);
//		printf("\n");
//		sleep(10);
//        while(1){
//        printf("connect with destination host...\n");
//        char info[] = "info:heartbeat-name:{}-status:open-number:5-time:";
//        send(clientSocket, info, sizeof(info)-1, 0);
//        }

//        char time[] = (char) (1+tmp_ptr->tm_mon);
//        strcpy(info, time);



//		if(strcmp(sendbuf, "quit") == 0)
//			break;


		iDataNum = recv(clientSocket, recvbuf, sizeof(recvbuf)-1, 0);
		recvbuf[iDataNum] = '\0';

//		判断是否为心跳包
		if (strcmp(recvbuf, "heartBeat") == 0){
//		    发送设备信息心跳包
		    char info[] = "info:heartbeat-name:{}-status:open-number:5-time:";
		    send(clientSocket, info, sizeof(info)-1, 0);
		    printf("是心跳包");
		    printf("recv data of my world is: %s\n", recvbuf);
            continue;
		}
		if(recvbuf[0] == '\0'){
		printf("断开连接");
		break;
		}
		else{
//		    操作指令
		    printf("不是心跳包");
		    printf("recv data of my world is: %s\n", recvbuf);
            continue;
		}
	}
	close(clientSocket);
	return 0;
}

