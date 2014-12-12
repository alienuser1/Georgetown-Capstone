import json
import pymongo
import glob
from pymongo import MongoClient

directory = '/gtown/data/*.json'
client = MongoClient("localhost", 27017)
db = client.twitter
collection = db.tweetloadertest

jsonFiles = glob.glob(directory)
for file in jsonFiles:
        f = open(file, 'r')
        for line in f.read().split("\n"):
                if line:
                        try:
                                lineJson = json.loads(line)
                        except (ValueError, KeyError, TypeError) as e:
                                pass
                        else:
                                postid = collection.insert(lineJson)
                                print 'inserted with id: ' , postid

        f.close()
