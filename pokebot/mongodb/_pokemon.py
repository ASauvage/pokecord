

class _Pokemon:
    def add_pokemon(self, pokemon_id: int, trainer_id: int) -> None:
        self.pokebot.pokemons.insert_one(dict(
            pokemon_id=pokemon_id,
            name=""
        ))
