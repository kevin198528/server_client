import socket
import subprocess

# udp_gb_server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 1060

network = '<broadcast>'

s.sendto('Client broadcast message!'.encode('utf-8'), (network, PORT))




# ip_port = ('127.0.0.1', 9997) # 定义元组
#
# s = socket.socket() # 绑定协义，生成套接字
# s.bind(ip_port) # 绑定 IP 端口，用来唯一标视一个进程, ip_port 必需是元组格式
# s.listen(5) # 定义最大可以挂起的连接数
#
# while True: # 用来重复接收新的连接
#
#     conn, addr = s.accept() # 接受客户端的连接请求,返还 conn (相当于一个特定的连接), addr 是客户端的 ip + port
#     print('get a new connection from %s' % str(addr))
#
#     while True: # 用来基于一个连接重复收发消息
#
#         try: # 捕捉客户端的异常关闭
#
#             recv_data = conn.recv(1024) # 收消息，阻塞
#             if len(recv_data) == 0:
#                 break # 客户端如果退出了，服务端将收到空消息，退出
#
#             p = subprocess.Popen(str(recv_data, encoding='utf8'), shell=True, stdout=subprocess.PIPE) # 执行系统命令
#             res = p.stdout.read()
#
#             if len(res) == '0':  # 执行错误命令，标准输出为空
#                 send_data = 'cmd err'
#             else:
#                 send_data = str(res, encoding='gbk') # 命令执行 ok, 字节 gbk --> str --> 字节 uft8
#
#             send_data=bytes(send_data,encoding='utf8')
#
#             # 为了解决粘包问题
#             ready_tag = 'Ready|%s' %len(send_data) # 生成
#             conn.send(bytes(ready_tag, encoding='utf8')) # 发送数据长度
#
#             feedback = conn.recv(1024) # Started 接收确认信息
#             feedback = str(feedback,encoding='utf8')
#
#
#             if feedback.startswith('Started'):
#                 conn.send(send_data) # 发送命令的执行结果
#
#         except Exception:
#             break
#
#     conn.close()
#     print('close connect from addr : %s\n' % str(addr))