from socket import *
import threading
import struct

ip_port = ("127.0.0.1", 8688)
MAX_DEV = 12

print("waiting for connection...")



def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    total_len = 0

    while True:
        data = sock.recv(RECV_SIZE)
        file_data = b""
        print(type(file_data))

        if len(data) is 0:
            print("disconnect")
            return

        print("data len is {}".format(len(data)))

        # check head len and content is valid
        if len(data) is not HEAD_SIZE:
            print("head len error")
            return

        head = struct.unpack("4sII", data)
        print(head)
        if head[0] != b"ICRD":
            print("head magic error")
            return

        sock.send(b"ready for recv")

        data_len = int(head[2])

        print("prepare for data len: {}".format(data_len))

        while data_len > 0:
            data_tmp = sock.recv(RECV_SIZE)
            file_data = file_data + data_tmp
            data_len = data_len - len(data_tmp)

        print(len(file_data))
        print(file_data)

        with open('./save/{}k'.format(int(len(file_data)/1024)), 'wb') as w_file:
            w_file.write(file_data)

        print("data len:{}".format(len(file_data)))

# while True:
#     print("before accept")
#     sock, addr = s_tcp_server.accept()
#     print("after accept")
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()


class ImageTransfer(object):
    def __init__(self):
        self.__s_socket = socket(AF_INET, SOCK_STREAM)
        self.__s_socket.bind(ip_port)

    @staticmethod
    def transfer_data(c_socket, c_addr):
        print('Accept new connection from %s:%s...' % c_addr)
        total_len = 0

        while True:
            data = c_socket.recv(RECV_SIZE)
            file_data = b""
            print(type(file_data))

            if len(data) is 0:
                print("disconnect")
                return

            print("data len is {}".format(len(data)))

            # check head len and content is valid
            if len(data) is not HEAD_SIZE:
                print("head len error")
                return

            head = struct.unpack("4sII", data)
            print(head)
            if head[0] != b"ICRD":
                print("head magic error")
                return

            sock.send(b"ready for recv")

            data_len = int(head[2])

            print("prepare for data len: {}".format(data_len))

            while data_len > 0:
                data_tmp = sock.recv(RECV_SIZE)
                file_data = file_data + data_tmp
                data_len = data_len - len(data_tmp)

            print(len(file_data))
            print(file_data)

            with open('./save/{}k'.format(int(len(file_data) / 1024)), 'wb') as w_file:
                w_file.write(file_data)

            print("data len:{}".format(len(file_data)))
        pass

    def get_one_frame(self):

    def start(self):
        self.__s_socket.listen(MAX_DEV)
        c_socket, c_addr = self.__s_socket.accept()
        t = threading.Thread(target=ImageTransferServer.transfer_data, args=(c_socket, c_addr))
        t.start()

# UDP socket

# max_size = 84*1024
#
# ip_port=('127.0.0.1', 8080)
# tcp_socket_server = socket(AF_INET,SOCK_DGRAM)
# tcp_socket_server.bind(ip_port)
# # tcp_socket_server.listen(5)
#
# # conn, addr = tcp_socket_server.accept()
# # data1 = conn.recv(10)
# # data2 = conn.recv(10)
#
# data1, address = tcp_socket_server.recvfrom(max_size)
#
#
# # print('----->', data1.dec)
# # conn.close()
#
# with open('./save/get_file_2.pdf', 'wb') as file:
#     file.write(data1)

# RECV_SIZE = 10*1024*1024
#
# HEAD_SIZE = 12


# TCP socket
