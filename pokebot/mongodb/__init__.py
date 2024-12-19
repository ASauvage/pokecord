import pymongo


class MongoCon(pymongo.MongoClient):
    def __init__(self, host: str = "mongodb://localhost:27017/"):
        super().__init__(host)

    from ._trainer import get_trainer_info, is_trainer_exist, create_trainer
    from ._pokemon import add_pokemon
    # from ._inventory import
