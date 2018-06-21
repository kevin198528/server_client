from socket import *
import threading
import time
import struct

ip_port = ("127.0.0.1", 8365)

RECV_SIZE = 8*1024*1024

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

# this is demo TX2 device
HEAD_SIZE = 12

if __name__ == "__main__":
    socket = socket(AF_INET, SOCK_STREAM)

    socket.connect(ip_port)
    file_data = b""
    socket.send(b"give one frame")

    print("a")

    data = socket.recv(RECV_SIZE)

    print("b")

    if len(data) is 0:
        print("disconnect")
        exit(-1)

    print("data len is {}".format(len(data)))

    # check head len and content is valid
    if len(data) is not HEAD_SIZE:
        print("head len error")
        exit(-1)

    head = struct.unpack("4sII", data)
    print(head)
    if head[0] != b"ICRD":
        print("head magic error")
        exit(-1)

    socket.send(b"ready for receive")

    data_len = int(head[2])

    print("prepare for data len: {}".format(data_len))

    while data_len > 0:
        data_tmp = socket.recv(RECV_SIZE)
        file_data = file_data + data_tmp
        data_len = data_len - len(data_tmp)

    print(len(file_data))

    with open('./save/{}k'.format(int(len(file_data) / 1024)), 'wb') as w_file:
        w_file.write(file_data)

    print("data len:{}".format(len(file_data)))
