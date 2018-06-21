import socket
import subprocess  # 执行命令模块
import threading
import time
import struct
from utils import *
# udp_gb_client.py

import socket
from utils import *


class GlobalInter(threading.Thread):
    dev_info = {}

    def __init__(self):
        super(GlobalInter, self).__init__()

        if not GlobalInter.dev_info:
            GlobalInter.dev_info = utils.load_config("./config/device.json")


class BroadInter(GlobalInter):
    def __init__(self):
        print("broadcast interface init")
        super(BroadInter, self).__init__()

        self.__dev_info = GlobalInter.dev_info

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind((self.__dev_info["broad_ip"], self.__dev_info["broad_port"]))
        print('Listening for broadcast at ', self.__socket.getsockname())

    def run(self):
        while True:
            data, address = self.__socket.recvfrom(self.__dev_info["broad_size"])
            print('Server received from {}:{}'.format(address, data.decode('utf-8')))
            self.__socket.sendto('deviceABC'.encode('utf-8'), address)


class AttrInter(GlobalInter):
    def __init__(self):
        print("attr interface init")


class ConnectInter(GlobalInter):
    def __init__(self, socket, addr):
        super(ConnectInter, self).__init__()
        self.__socket = socket
        self.__addr = addr
        self.__dev_info = GlobalInter.dev_info
        self.__recv_size = self.__dev_info["frame_size"]
        self.__request_cmd = b"give one frame"
        self.__ready_cmd = b"ready for receive"
        self.__head_size = 12

        with open('./img/30kk.pdf', 'rb') as file:
            self.__content = file.read()

    def run(self):
        print('Accept new connection from {}...'.format(self.__addr))

        while True:
            recv_data = self.__socket.recv(self.__recv_size)
            if len(recv_data) is 0 or recv_data != self.__request_cmd:
                print("len 0 or valid request continue")
                return

            print(recv_data)

            # send the head
            head = struct.pack("4sII", b"ICRD", 1, len(self.__content))
            self.__socket.send(head)

            # check head response is valid
            recv_data = self.__socket.recv(self.__recv_size)
            if len(recv_data) is 0 or recv_data != self.__ready_cmd:
                print("len 0 or valid ready cmd continue")
                return

            print(recv_data)

            # send all data
            self.__socket.sendall(self.__content)


class FrameInter(GlobalInter):
    def __init__(self):
        print("frame interface init")
        super(FrameInter, self).__init__()

        self.__dev_info = GlobalInter.dev_info

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__dev_info["frame_ip"], self.__dev_info["frame_port"]))
        self.__socket.listen(5)
        print('Listening for frame request ... ', self.__socket.getsockname())

    def run(self):
        while True:
            print("frame channel waiting for connect")
            socket, addr = self.__socket.accept()
            print("a new connect create")
            con_ins = ConnectInter(socket, addr)
            con_ins.start()


if __name__ == "__main__":
    df_ins = BroadInter()
    df_ins.start()

    fr_ins = FrameInter()
    fr_ins.start()

    while True:
        time.sleep(10)
