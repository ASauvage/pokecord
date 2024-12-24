

class _Inventory:
    def get_inventory(self, trainer_id: int) -> dict:
        return self.pokebot.trainers.find_one({'trainer_id': trainer_id}, {'inventory': 1})

    def change_item_quantity(self, trainer_id: int, item: str, operation: int) -> None:
        self.pokebot.trainers.update_one({'trainer_id': trainer_id}, {'$inc': {f'inventory.{item}': operation}})
