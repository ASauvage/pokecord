from datetime import date


class _Trainer:
    def get_trainer_info(self, trainer_id: int) -> dict:
        return self.pokebot.trainers.find_one({'trainer_id': trainer_id}, {'inventory': 0, 'pokemon_team': 0})

    def is_trainer_exist(self, trainer_id: int) -> bool:
        return bool(self.pokebot.trainers.find_one({'trainer_id': trainer_id}))

    def create_trainer(self, trainer_id: int, trainer_team: str) -> None:
        self.pokebot.trainers.insert_one(dict(
            trainer_id=trainer_id,
            register_since=date.today().isoformat(),
            trainer_team=trainer_team,
            trainer_lvl=dict(
                lvl=1,
                exp=0,
                required=50
            ),
            stats=dict(
                battle_won=0,
                pokemon_caught=0
            ),
            inventory=dict(
                pokeball=0,
                superball=0,
                hyperball=0,
                masterball=0,
                potion=0,
                super_potion=0,
                hyper_potion=0,
                max_potion=0
            ),
            pokemon_team=list()
        ))
