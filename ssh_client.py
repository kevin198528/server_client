# Author: Janice Cheng

import socket
import subprocess  # 执行命令模块

# udp_gb_client.py
'''客户端（UDP协议局域网广播）'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

s.bind(('', PORT))
print('Listening for broadcast at ', s.getsockname())

while True:
    data, address = s.recvfrom(65535)
    print('Server received from {}:{}'.format(address, data.decode('utf-8')))

# ip_port = ('127.0.0.1', 9997)  # 定义元组
# s = socket.socket()  # 绑定协义，生成套接字
# s.connect(ip_port)  # 连接服务端，如果服务端已经有一个连接的话，就立即挂起
#
# while True:  # 基于 s.connect() 建立的连接来循环发消息
#
#     send_data = input(">>: ").strip()
#     if send_data == 'exit':
#         break
#
#     if len(send_data) == 0:
#         continue
#
#     s.send(bytes(send_data, encoding='utf8'))
#
#     # 为了解决粘包问题
#     ready_tag = s.recv(1024)  # 获取数据长度的字节 Ready|9998
#     ready_tag = str(ready_tag, encoding='utf8')
#     if ready_tag.startswith('Ready'):  # Ready|9998
#         msg_size = int(ready_tag.split('|')[-1])  # 获取待接收数据
#
#     start_tag = 'Started'  # 发送确认信息
#     s.send(bytes(start_tag, encoding='utf8'))
#
#     # 基于已经收到的待接收数据长度，循环接收消息
#     recv_size = 0
#     recv_msg = b''
#
#     while recv_size < msg_size:
#         recv_data = s.recv(1024)
#         recv_msg += recv_data
#         recv_size += len(recv_data)
#         print("Msg Size %s Recv Size %s" % (msg_size, recv_size))
#
#     print(str(recv_msg, encoding='utf8'))
#
# s.close()
