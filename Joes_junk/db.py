from pymongo import MongoClient
from chirpy.config import settings

def connect(**kwargs):
    defaults = {
        'host': settings.mongo.get('host'),
        'port': settings.mongo.get('port')
    }
    defaults.update(kwargs)

    client = MongoClient(**defaults)
    return client[settings.mongo.database]
    
if __name__ == '__main__':
    db = connect()
    db.tweets.count()
