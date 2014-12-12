from pymongo import MongoClient
conn = MongoClient ()
db = conn.GtownTwitter
tweets_collection = db.tweets_collection
for tweet in tweets_collection.find ():
     print tweet ['text']
