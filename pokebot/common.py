import os
import json


class TrainerNotFound(Exception):
    def __init__(self, trainer_id):
        super().__init__(f"No account found for trainer_id: {trainer_id}")


def get_commands_list():
    with open(os.path.dirname(__file__) + '/commands.json', 'r') as json_file:
        return json.load(json_file)
