import pymongo


class MongoCon(pymongo.MongoClient):
    def __init__(self, host: str = "mongodb://localhost:27017/"):
        super().__init__(host)
