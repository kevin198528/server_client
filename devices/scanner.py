import socket
import time, threading
import sys
import struct

# root_path = "/home/zjq/PycharmProjects/server_client/server_client/"
# sys.path.append(root_path)

from utils import *

# from ../utils import *
#
# from uti

cmd = {'bc_cmd': 'give_your_info'}
# must use jue dui path


def py_print(str):
    print("python: " + str)


class AbsDevice(object):
    def __init__(self, name):
        self.__name = name
        self.__open_flag = False
        # self.__id = id

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__recv_size = 8*1024*1024
        self.__head_size = 12

    def get_name(self):
        return self.__name

    # open a tcp connection
    def dev_open(self):
        if not self.__open_flag:
            print("device open")
            self.__open_flag = True
            self.__socket.connect(("127.0.0.1", 8365))

    def dev_close(self):
        print("device close")
        self.__open_flag = False
        self.__socket.close()

    def dev_getframe(self):
        if not self.__open_flag:
            print("device not open")
            return
        else:
            print("start to get one frame")
            frame_data = b""
            self.__socket.send(b"give one frame")

            data = self.__socket.recv(self.__recv_size)
            if len(data) is 0:
                print("len 0 disconnect")
                self.dev_close()
                return

            print("data len is {}".format(len(data)))

            # check head len and content is valid
            if len(data) is not self.__head_size:
                print("head len error")
                return

            head = struct.unpack("4sII", data)
            print(head)
            if head[0] != b"ICRD":
                print("head magic error")
                return

            self.__socket.send(b"ready for receive")

            data_len = int(head[2])

            print("prepare for data len: {}".format(data_len))

            while data_len > 0:
                data_tmp = self.__socket.recv(self.__recv_size)
                frame_data = frame_data + data_tmp
                data_len = data_len - len(data_tmp)

            print(len(frame_data))

            return frame_data
            # with open('./save/{}k'.format(int(len(file_data) / 1024)), 'wb') as w_file:
            #     w_file.write(file_data)
            #
            # print("data len:{}".format(len(file_data)))


class Scanner(object):
    def __init__(self):
        print("scanner init")
        self.config = utils.load_config("/home/zjq/PycharmProjects/server_client/config/scanner.json")
        self.scan_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.scan_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # self.scan_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO)
        self.scan_socket.settimeout(0.05)
        self.ip_bc = self.config["ip_bc"]
        self.port_bc = self.config["port_bc"]
        self.addr_bc = (self.ip_bc, self.port_bc)
        self.rec_size = 5600

    def scanning(self):
        py_print("scanning start")
        self.dev_list = []
        self.scan_socket.sendto(utils.dict2json(cmd), self.addr_bc)

        for _ in range(12):
            try:
                data, addr = self.scan_socket.recvfrom(self.rec_size)
            except socket.timeout:
                print("socket receive from time out")
            else:
                name = data.decode('utf-8')
                py_print(name)
                camera_dev = AbsDevice(name)
                self.dev_list.append(camera_dev)
                print(type(name))
                print(name)
                print(addr)

        print(self.dev_list)
        py_print("scanning stop")
        return self.dev_list


if __name__ == '__main__':
    # utils.utils
    # print(utils.__init__)
    # for t in sys.argv:
    #     print(t)
    #
    # print(sys.path)

    sc = Scanner()
    dev_list = sc.scanning()

    dev = dev_list[0]

    # dev = AbsDevice("deviceA")
    dev.dev_open()

    frame = dev.dev_getframe()

    dev.dev_close()

    print(len(frame), type(frame))

    time.sleep(1000)

    # dev_monitor = DmMonitor(dev_info)
    # scanner_info = load_config("../config/scanner.json")
    # print(scanner_info)
