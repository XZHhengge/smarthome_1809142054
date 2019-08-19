# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/8/19
#   多线程服务器（心跳包版）
#   hreatBeat_Server.py
import socket
import select
import threading
import time


# 心跳包线程
def hreatBeat(conn):
    sum = 0  # 无回应次数
    while True:
        time.sleep(10)
        if sum < 3:
            try:
                conn.sendall(bytes("hreatBeat".encode('utf-8')))
                sum = 0
            except socket.error:
                sum = sum + 1
                continue
        else:
            conn.close()
            break


def process(tcpCliSock, addr):
    print("connect from " + str(addr))

    pattern_data = tcpCliSock.recv(1024)
    print(pattern_data)

    tcpCliSock.sendall(bytes("here is server".encode('utf-8')))
    #  创建心跳包线程
    #  须记住，创建新线程时 args参数如果只有一个的话一定要加个逗号！！
    thr = threading.Thread(target=hreatBeat, args=(tcpCliSock,))
    thr.start()
    #  thr.is_alive() 用于监测进程thr是否还存在（即client是否还在连接中）
    while thr.is_alive():
        # print(pattern_data)
        print("do everything you like here")



def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 33333))
    server.listen(5)
    while True:
        r, w, e = select.select([server, ], [], [], 1)
        # enumerate()分别列举出list r中的序号和内容
        for i, server in enumerate(r):
            conn, addr = server.accept()
            t = threading.Thread(target=process, args=(conn, addr))
            t.start()


if __name__ == "__main__":
    run()
