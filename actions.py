import json


def parse_string(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    return data

