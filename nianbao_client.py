from socket import *
import threading
import time
import struct

ip_port = ("127.0.0.1", 8688)

RECV_SIZE = 1024

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

# with open('./img/30kk.pdf', 'rb') as file:
#     read_file = file.read()
#
#     print(len(read_file))
#
#     # s_tcp_client.sendto(read_file, ip_port)
#
#     s_tcp_client.send(read_file)
#
#     time.sleep(1000)

# s_tcp_client.send(b"hello")
#
# s_tcp_client.send(b"world")
#
# print(int("0x5A5A", 16))
# print(hex(23130))


with open('./img/30kk.pdf', 'rb') as file:
    # content = b"hello"
    # magic(2bytes) version(2bytes) length(4bytes)
    # content = file.read()

    content = b"hello world"

    print(len(content))

    b = struct.pack("4sII", b"ICRD", 1, len(content))

    s_tcp_client.send(b)

    data = s_tcp_client.recv(RECV_SIZE)

    print("get response")
    print(data)

    if data == b"ready for recv":
        print("send content")
        s_tcp_client.sendall(content)


