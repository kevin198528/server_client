import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT = 6363

network = '<broadcast>'

cmd = {'cmd': 'get_dev_info'}

json_cmd = json.dumps(cmd)

s.sendto(json_cmd.encode('utf-8'), (network, PORT))

data, address = s.recvfrom(5600)
print('Server received from {}:{}'.format(address, json.loads(data.decode('utf-8'))))
