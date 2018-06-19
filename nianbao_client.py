from socket import *
import threading
import time

ip_port = ("127.0.0.1", 8686)

# BUFSIZE=1024
# ip_port=('127.0.0.1',8080)
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # res = s.connect_ex(ip_port)
#
# with open('./img/84k.pdf', 'rb') as file:
#     read_file = file.read()
#
#     print(len(read_file))
#
#     s.sendto(read_file, ip_port)

# s.send('hello'.encode('utf-8'))
# s.send('feng'.encode('utf-8'))


s_tcp_client = socket(AF_INET, SOCK_STREAM)

s_tcp_client.connect(ip_port)

# with open('./img/14kk.pdf', 'rb') as file:
#     read_file = file.read()
#
#     print(len(read_file))
#
#     # s_tcp_client.sendto(read_file, ip_port)
#
#     s_tcp_client.send(read_file)
#
#     time.sleep(1000)

s_tcp_client.send(b"hello")

s_tcp_client.send(b"world")