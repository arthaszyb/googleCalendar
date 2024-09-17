import json

def load_conf(file_name = 'conf/conf.json'):
    with open(file_name, 'r') as file:
        config = json.load(file)
    return config
