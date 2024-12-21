

class _Inventory:
    def get_inventory(self, trainer_id: str) -> dict:
        return self.pokebot.trainers.find_one({'trainer_id': trainer_id}, {'inventory': 1})
