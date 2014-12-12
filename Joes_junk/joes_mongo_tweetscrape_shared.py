#__author__ = 'cf652d'

# Scrapes tweets with keyword search and writes to mongo DB "tweets", collection "tweetcollection"
#
import pymongo
import tweepy, json, pprint, time
from tweepy.api import API
from pymongo import MongoClient
client = MongoClient()
from db import connect
#
consumer_key = ""
API_KEY = ""
consumer_secret = ""
API_SECRET = ""
access_token = ""
access_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
key = tweepy.OAuthHandler(API_KEY, API_SECRET)
key.set_access_token(access_token, access_secret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

key = tweepy.OAuthHandler(API_KEY, API_SECRET)

key.set_access_token(access_token, access_secret)

#

class Stream2Screen(tweepy.StreamListener):
    def __init__(self, api=None):
        self.api = api or API()
        self.db      = connect()
        self.n = 0
        self.m = 1000 ##number of tweets
        timestr = time.strftime("%Y%m%d_%H%M%S")
        fname = '/gtown/data/json_tweepy%s.txt'% timestr
        self.output = open(fname, 'w') ##writes to file

    def on_data(self, data):
        datadict = json.loads(data)
        #pprint.pprint(datadict, self.output)
        #self.output.write(data)    ##writes to file, not pretty print in above line
        self.db.tweetcollection.insert(datadict)  ##writes to mongo
        self.n = self.n+1
        if self.n < self.m: return True
        else:
            self.output.close()    ##output file close
            print 'tweets = '+str(self.n)
            return False




stream = tweepy.streaming.Stream(key, Stream2Screen())
stream.filter(track=['ISIS'], languages=['en'])



