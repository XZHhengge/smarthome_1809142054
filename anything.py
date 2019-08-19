# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/7/27
import socket
import time
import threading
from datetime import datetime
import json
def tcp(name):
    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.settimeout(10)

    # 获取本地主机名
    host = '127.0.0.1'

    # 设置端口号
    port = 33333
    # 连接服务，指定主机和端口
    s.connect((host, port))
    while True:
        # 发送心跳包
        # info = {
        #     'name': '',
        #     'info': 'test',
        #     'status': 'safe',
        #     'number': data,
        #     'time': str(datetime.now())
        # }  # json数据,这是我们要暂时定义好要发的数据,不同wifi模块的Number是不一样的,你可以定义编号

        json_info = 'info:heartbeat-name:{}-status:open-number:5-time:{}'.format(name, datetime.now())
        s.send(bytes(json_info.encode('utf-8')))
        time.sleep(5)
        msg = s.recv(1024).decode('utf-8')
        if msg == 'heartbeat':
            print('server接收心跳包成功')
        else:
            print('下发指令:', msg)

        # 接收小于 1024 字节的数据

        # try:

            # msg = str(msg, encoding='utf-8')
            # name = json.loads(msg)['name']
            # if name == '':
            #     continue
            # else:
            #     print('api传参数')






    # s.close()

if __name__ == '__main__':
    number = ['xxxx', 'yyyy', 'zzzz', 'bbbb']
    for i in number:
        t = threading.Thread(target=tcp, args=(i,))
        t.start()
