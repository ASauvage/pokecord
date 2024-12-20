from . import MongoCon


def get_inventory(self: MongoCon, trainer_id: str) -> dict:
    return self.pokebot.trainers.find_one({'trainer_id': trainer_id}, {
        'trainer_id': 0,
        'register_since': 0,
        'trainer_team': 0,
        'trainer_level': 0,
        'stats': 0,
        'pokemon_team': 0
    })
