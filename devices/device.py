import socket
import time, threading
import json


print(type(socket))
print(socket.__dict__)

time.sleep(100)

# slave_info = {
#     "type": "slave",
#     "name": "tx2 camera 01",
#     "id": "00-01",
#     "broadcast_channel_info": {
#         "port": 6363,
#         "max_size": 65535
#     },
#     "control_channel_info": {
#       "ip": "127.0.0.1",
#       "port": 6383,
#       "type": "udp",
#       "max_size": 65535
#     },
#     "stream_channel_info": {
#       "ip": "127.0.0.1",
#       "port": 6386,
#       "type": "tcp"
#     }
# }
#
# # <broadcast>
# master_info = {
#     "type": "master",
#     "name": "pc master 01",
#     "id": "01-01",
#     "broadcast_channel_info": {
#         "ip": "<broadcast>",
#         "port": 6363,
#         "type": "udp"
#     }
# }


class Config(object):
    @staticmethod
    def load_config(json_path):
        with open(json_path, "r") as j_file:
            dev_info = json.loads(j_file.read())

        return dev_info


class CameraDevice(object):
    def __init__(self, dev_info):
        # self.__m_thread = None
        # self.__ip = ''
        # self.__port = 6363
        # self.__max_size = 65535
        self.__dev_info = dev_info

        # socket for listen broadcast
        self.__socket_broadcast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.__socket_broadcast.bind(("", self.__dev_info["broadcast_channel_info"]["port"]))

        print('device manager - monitor - Listening for broadcasting', self.__socket_broadcast.getsockname())

        # self.__m_thread = threading.Thread(target=self.monitor_thread_loop, name='monitor_thread_loop')
        #
        # self.__m_thread.start()
        # self.__m_thread.join()

    def start(self):
        while True:
            utf8_data, address = self.__socket_broadcast.recvfrom(self.__dev_info["broadcast_channel_info"]["max_size"])

            data = json.loads(utf8_data.decode('utf-8'))

            print(data)

            if data['cmd'] == 'get_dev_info':
                print('send dev info to {}'.format(address))
                self.__socket_broadcast.sendto(json.dumps(self.__dev_info).encode('utf-8'), address)
            # print('Server received from {}:{}'.format(address, data.decode('utf-8')))

    # def monitor_thread_loop(self):
    #     while True:
    #         utf8_data, address = self.__s.recvfrom(self.__max_size)
    #
    #         data = json.loads(utf8_data.decode('utf-8'))
    #
    #         print(data)
    #
    #         if data['cmd'] == 'get_dev_info':
    #             print('send dev info to {}'.format(address))
    #             self.__s.sendto(self.__json_dev_info.encode('utf-8'), address)
    #         # print('Server received from {}:{}'.format(address, data.decode('utf-8')))


if __name__ == "__main__":
    print("camera device start")

    # dev_monitor = CameraDevice(dev_info)
    dev_info = Config.load_config("./camera_device.json")
    CameraDevice(dev_info).start()

