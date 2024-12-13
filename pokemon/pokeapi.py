from requests import JSONDecodeError, get


class PokeAPI:
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/{endpoint}'

    def get_pokemon_by_id(self, id: int) -> dict:
        """
        Get Pokémon details by using their IDs

        :param id: Pokémon's ID
        """
        try:
            return get(self.url.format(endpoint=f'pokemon/{id}')).json()
        except JSONDecodeError as e:
            raise e
