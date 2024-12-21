import pymongo
from ._trainer import _Trainer
from ._pokemon import _Pokemon
from ._inventory import _Inventory


class MongoCon(pymongo.MongoClient, _Trainer, _Pokemon, _Inventory):
    def __init__(self, host: str = "mongodb://localhost:27017/"):
        super().__init__(host)

