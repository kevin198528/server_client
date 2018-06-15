import json


def print_u():
    print("hello utils")


def load_config(json_path):
    with open(json_path, "r") as j_file:
        dev_info = json.loads(j_file.read())
        return dev_info


def dict2json(in_dict):
    return json.dumps(in_dict).encode('utf-8')