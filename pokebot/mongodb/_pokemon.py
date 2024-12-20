from . import MongoCon


def add_pokemon(self: MongoCon, pokemon_id: int, trainer_id: str) -> None:
    self.pokebot.pokemons.insert_one(dict(
        pokemon_id=pokemon_id,
        name=""
    ))
