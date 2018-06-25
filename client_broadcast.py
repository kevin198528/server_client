import socket
import subprocess  # 执行命令模块
import threading
import time
import struct
import json
from utils import *
# udp_gb_client.py

import socket
from utils import *

device_info = {
    "name": "tx2 camera A",
    "id": "01",

    "broad_ip": "",
    "broad_port": 8363,
    "broad_size": 65535,

    "frame_ip": "127.0.0.1",
    "frame_port": 6365,
    "frame_size": 65535,

    "ctrl_ip": "127.0.0.1",
    "ctrl_port": 6368,
    "ctrl_size": 65535
}

cmd_get_info = "give_your_info"

def print_u():
    print("hello utils")


def load_config(json_path):
    with open(json_path, "r") as j_file:
        dev_info = json.loads(j_file.read())
        return dev_info


def dict2json(in_dict):
    return json.dumps(in_dict).encode('utf-8')


class GlobalInter(threading.Thread):
    dev_info = {}

    def __init__(self):
        super(GlobalInter, self).__init__()

        if not GlobalInter.dev_info:
            # GlobalInter.dev_info = utils.load_config("./config/device.json")
            GlobalInter.dev_info = device_info


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

            print(data, type(data))

            get_cmd = data.decode('utf-8')
            print(get_cmd, cmd_get_info)
            print(type(get_cmd), type(cmd_get_info))
            print('Server received from {}:{}'.format(address, get_cmd))
            if data.decode('utf-8') == cmd_get_info:
                self.__socket.sendto(dict2json(self.__dev_info), address)
            else:
                print("valid cmd")


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
            print(recv_data, len(recv_data))
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
