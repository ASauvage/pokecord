import os
import json


def get_commands_list():
    with open(os.path.dirname(__file__) + '/commands.json', 'r') as json_file:
        return json.load(json_file)
