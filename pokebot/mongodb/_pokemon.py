from bson.objectid import ObjectId


class _Pokemon:
    def get_pokemon(self, _id: str) -> dict:
        return self.pokebot.pokemons.find_one({'_id': ObjectId(_id)})

    def get_pokemons(self, trainer_id: int) -> list:
        return self.pokebot.trainers.aggregate([
            {'$match': {'trainer_id': trainer_id}},
            {'$lookup': {'from': 'trainers', 'localField': 'pokemon_team', 'foreignField': '_id', 'as': 'pokemon_team'}},
            {'pokemon_team': 1}
        ])['pokemon_list']

    def add_pokemon(self, trainer_id: int, pokedex_number: int, name: str = None) -> None:
        pokemon_id = self.pokebot.pokemons.insert_one(dict(
            pokedex_number=pokedex_number,
            name=name,
            pokemon_lvl=dict(
                lvl=1,
                exp=0,
                exp_required=50
            ),
            hp=100,
            stats={'att': 15, 'def': 15, 'att_spe': 15, 'def_spe': 15, 'spd': 15},
            iv={'att': 15, 'def': 15, 'att_spe': 15, 'def_spe': 15, 'spd': 15}
        ))

        self.pokebot.trainers.update_one({'trainer_id': trainer_id}, {'$push': {'pokemon_team': ObjectId(pokemon_id)}})

    def remove_pokemon(self, trainer_id: int, _id: str) -> None:
        self.pokebot.trainers.update_one({'trainer_id': trainer_id}, {'$pull': {'pokemon_team': ObjectId(_id)}})
        self.pokebot.pokemons.delete_one({'_id': ObjectId(_id)})
