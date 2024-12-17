from .pokeapi import PokeAPI


class PokeData:
    def __init__(self, id: int):
        self.pokeapi_data = PokeAPI().get_pokemon_by_id(id)

    @property
    def number(self) -> int:
        return self.pokeapi_data['number']

    @property
    def name(self) -> str:
        return self.pokeapi_data['name']


class Pokemon(PokeData):
    def __init__(self, id: int):
        self._id = id
        self.pokemon = dict()
        super().__init__(self.pokemon['number'])

    @property
    def nickname(self) -> str | None:
        return self.pokemon['nickname']

    @property
    def sexe(self) -> bool:
        return self.pokemon['sexe']

    @property
    def level(self) -> int:
        return self.pokemon['level']
