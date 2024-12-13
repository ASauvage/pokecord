from .pokeapi import PokeAPI


class Pokemon:
    def __init__(self, id: int):
        self._id = id
        self.pokemon = PokeAPI.get_pokemon_by_id(id)

    @property
    def name(self) -> str:
        return self.pokemon['name']
