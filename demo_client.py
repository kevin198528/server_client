from collections import Iterable
import json


class RawDevice(object):
    def __init__(self):
        self.__name = 'camera dev'
        self.__ip = '127.0.0.1'
        self.__port = '8888'

    def set_name(self):
        pass

    def get_name(self):
        pass

    def set_frame_rate(self):
        pass

    def get_frame_rate(self):
        pass

    def set_attribute(self, index, value):
        pass

    def get_attribute(self, index, value):
        pass


class CameraScanner(object):
    def __init__(self):
        print('camera scanner init')

    def scan(self):
        dev_list = [{'dev_id': 1}, {'dev_id': 2}, {'dev_id': 3}]
        return dev_list


class MasterDevice(RawDevice):
    def __init__(self):
        pass

    def scan(self):
        pass


class SlaveDevice(RawDevice):
    def __init__(self):
        pass

ins_scanner = CameraScanner()

dev_list = ins_scanner.scan()

for dev in dev_list:
    print(dev['dev_id'])


# with open('./conf.json') as file:
#     data = json.loads(file.read())

dev_attr_list = {}

dev_attr_list['addr'] = {'ip': '127.0.0.1', 'port': '8888'}

json_data = json.dumps(dev_attr_list)

data = json.loads(json_data)

CameraDev.set_attribute('frame_rate', '15')

CameraDev.set_attribute('dev_name', '001')



print(json_data)

print(data['addr']['ip'])

