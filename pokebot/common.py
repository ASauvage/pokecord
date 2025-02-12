import os
import json


class TrainerNotFound(Exception):
    def __init__(self, trainer_id):
        super().__init__(f"No account found for trainer_id: {trainer_id}")


def get_commands_list(cog: str = None):
    if cog is None:
        commands = dict()
        for file in os.listdir(f'{os.path.dirname(__file__)}/cogs/'):
            if file.endswith('.json'):
                with open(f'{os.path.dirname(__file__)}/cogs/{file}', 'r') as json_file:
                    commands = commands | json.load(json_file)

        return commands

    else:
        with open(f'{os.path.dirname(__file__)}/cogs/{cog}.json', 'r') as json_file:
            return json.load(json_file)
