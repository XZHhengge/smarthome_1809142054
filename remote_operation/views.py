# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required  # 登录访问限制
from django.http import HttpResponse  # HTTP响应
from django.http import JsonResponse  # JSON响应
# import models

import time

from remote_operation.models import Device
from remote_operation.udp_service import udp_server
import socket
import json
import struct
import threading
import select


# Create your views here.
# from udp_server import udp_handler

def get_equipment_status(self, *args):

    first_type = args[0]
    second_type = args[1]
    device_number = args[2]
    '''获取一台在线设备的状态'''
    response = {}
    equipment_status = udp_server.get_equipment_status(first_type, second_type, device_number)
    if equipment_status:
        response['code'] = 0
        response['msg'] = 'Success'
        response['status'] = equipment_status
        return JsonResponse(response)
    else:
        response['code'] = 1
        response['msg'] = 'Fail, The target device has been off-line.'
        return JsonResponse(response)


def get_online_equipment(request):
    '''获取当前在线设备信息'''
    response = {}
    eqipment_list = udp_server.get_online_equipment()
    response['code'] = 0
    response['msg'] = 'Success'
    response['equipment_list'] = eqipment_list
    return JsonResponse(response)


def control_light(request):
    '''电灯控制'''
    response = {}
    # 此处选用get方法而不用字典方法取值可以默认返回None(可自定义)
    number = request.GET.get('number')
    operation = request.GET.get('operation')
    if udp_server.control_light(number, operation):
        response['code'] = 0
        response['msg'] = 'Success'
        return JsonResponse(response)
    else:
        response['code'] = 1
        response['msg'] = 'Fail, The target device has been off-line or command error.'
        return JsonResponse(response)
    response['code'] = 0
    response['msg'] = 'Success'
    return JsonResponse(response)


def control_fan(request):
    '''电扇控制'''
    response = {}
    number = request.GET.get('number')
    operation = request.GET.get('operation')
    if udp_server.control_fan(number, operation):
        response['code'] = 0
        response['msg'] = 'Success'
        return JsonResponse(response)
    else:
        response['code'] = 1
        response['msg'] = 'Fail, The target device has been off-line or command error.'
        return JsonResponse(response)


def control_curtain(request):
    '''窗帘控制'''
    response = {}
    number = request.GET.get('number')
    operation = request.GET.get('operation')
    if udp_server.control_curtain(number, operation):
        response['code'] = 0
        response['msg'] = 'Success'
        return JsonResponse(response)
    else:
        response['code'] = 1
        response['msg'] = 'Fail, The target device has been off-line or command error.'
        return JsonResponse(response)


def control_air_conditioner(request):
    '''空调控制'''
    response = {}
    number = request.GET.get('number')
    model = request.GET.get('model')
    operation = request.GET.get('operation')
    if udp_server.control_air_conditioner(number, model, operation):
        response['code'] = 0
        response['msg'] = 'Success'
        return JsonResponse(response)
    else:
        response['code'] = 1
        response['msg'] = 'Fail, The target device has been off-line or command error.'
        return JsonResponse(response)

flag = False
global udp_socket
from datetime import datetime
def udp(request, data):
    device = Device.objects.get(number=data)  # 查询设备号
    global udp_socket
    info = {
        'name': data,
        'info': 'api',
        'status': '1',
        'number': '',
        'time': str(datetime.now())
    }
    json_info = json.dumps(info)
    udp_socket.sendto(bytes(json_info.encode('utf-8')), eval(device.ip_port))
    time.sleep(1)
    if flag:
        return HttpResponse('success')
    else:
        return HttpResponse('failure')

def udp_handler():
    global udp_socket
    # try:
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('0.0.0.0', 23333))
    # udp_socket.settimeout(5)
    print("waiting to receive messages...")
    while True:
        udp_data, ip_address = udp_socket.recvfrom(1024)
        id, tag, version, count = struct.unpack("!Hc2I", udp_data)
        print(id, tag, version, count, ip_address)
        str_data = str(udp_data, encoding='utf-8')
        print(str_data)
        number = json.loads(str_data)['number']
        name = json.loads(str_data)['name']
        # 获取线程ip和地址
        if Device.objects.filter(number=number):
            device = Device.objects.get(number=number)
            device.ip_port = ip_address
            device.save()
        else:
            # print(ip_address)
            Device.objects.create(number=number, ip_port=ip_address).save()
        if name == '':
            # print('心跳包', datetime.now())
            # 这里要设置重传机制
            udp_socket.sendto(udp_data, ip_address)
            # time.sleep(1)
            continue
        else:
            global flag
            flag = True
            print('api调用接口返回成功', datetime.now())

def tcp_handler():
    serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

    # 获取本地主机名
    host = socket.gethostname()

    port = 9999

    # 绑定端口号
    serversocket.bind((host, port))

    # 设置最大连接数，超过后排队
    serversocket.listen(5)

    while True:
        # 建立客户端连接
        clientsocket, addr = serversocket.accept()

        print("连接地址: %s" % str(addr))

        msg = '欢迎访问菜鸟教程！' + "\r\n"
        clientsocket.send(msg.encode('utf-8'))
        clientsocket.close()

def index(request):
    # print('启动UDP处理线程')
    # udp_thread = threading.Thread(target=udp_handler)
    udp_thread = threading.Thread(target=run)
    udp_thread.setDaemon(True)
    udp_thread.start()
    # run()
    return HttpResponse('success')

# global tcpCliSock

def hreatBeat(tcpCliSock):
    sum = 0  # 无回应次数
    while True:
        time.sleep(10)
        if sum < 3:
            try:
                tcpCliSock.sendall(bytes("heartBeat".encode('utf-8')))  #心跳包
                # global tcpCliSock
                sum = 0
            except socket.error:
                sum = sum + 1
                continue
        else:
            tcpCliSock.close()
            print('break')
            #添加导数据库
            continue


def process(tcpCliSock, addr):
    # global tcpCliSock
    print("connect from " + str(addr))

    tcpCliSock.sendall(bytes("here is server".encode('utf-8')))
    # pattern_data = tcpCliSock.recv(1024)
    #  创建心跳包线程
    #  须记住，创建新线程时 args参数如果只有一个的话一定要加个逗号！！
    thr = threading.Thread(target=hreatBeat, args=(tcpCliSock,))
    thr.start()
    #  thr.is_alive() 用于监测进程thr是否还存在（即client是否还在连接中）
    while thr.is_alive():
        pattern_data = tcpCliSock.recv(1024)
        pattern_data = str(pattern_data, encoding='utf-8')
        if pattern_data[5:14] == 'heartbeat':
            print('心跳包')
            continue
        else:
            print(pattern_data)
            print('接收设备指令')
            continue
        # print(pattern_data)
        # print(pattern_data)
        # print("do everything you like here")
    else:
        print('client已断开')
global conn

def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 5555))
    server.listen(5)
    while True:
        r, w, e = select.select([server, ], [], [], 1)
        # enumerate()分别列举出list r中的序号和内容
        for i, server in enumerate(r):
            global conn
            conn, addr = server.accept()
            t = threading.Thread(target=process, args=(conn, addr))
            t.start()

def tcp(request, data):
    global conn
    conn.sendall(bytes(data.encode('utf-8')))
    return HttpResponse('success')


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
global s
def run2():
    global s
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

def tcpsend2(request, data):
    global s
    s.sendall(bytes(data.encode('utf-8')))
    return HttpResponse('success')
