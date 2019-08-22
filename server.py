# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/8/19
import time
import socket
import threading
from datetime import datetime

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        print(data)
        # 接收心跳包
        if data.decode('utf-8')[5:14] == 'heartbeat':
            print('心跳包')
            sock.send(bytes('heartbeat{}'.format(datetime.now()).encode('utf-8')))
            continue
        elif data == '':
            break
        else:
            print('指令下发回传')
            continue
        # if not data or data.decode('utf-8') == 'exit':
        #     break
        # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    # sock.close()
    # print('Connection from %s:%s closed.' % addr)

# 创建 socket 对象
def run2():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('127.0.0.1', 5555))
    s.listen(5)
    print('Waiting for connection...')

    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
