# Load twython library
import json  # Teach python JSON
from twython import Twython, TwythonError, TwythonStreamer # Load libraries for twitter API
import pymongo # Teach python to talk to MongoDB
# Setup Authentificaion Settings
APP_KEY = '' # Consumer key
APP_SECRET = '' # Consumer secret
OAUTH_TOKEN = ''  # Access token
OAUTH_TOKEN_SECRET = ''  # Access tocen secret
# Obtain an OAuth 2 Access Token
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
# Use the Access Token
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
# Setup a connection to mongodb
connection = pymongo.Connection('localhost', 27017)
db = connection.joe
# Define a class to handle the stream
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            db.twaats.save(data) # Take the data in text and save it to the mongodb twitter.tweets
    def on_error(self, status_code, data):
        print status_code, data
# Start the stream
# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#stream.statuses.filter(locations = '-74,40,-73,41') # Get tweets from a specific location e.g. New York City
stream.statuses.filter(track=['isis'], languages=['en']) # Get tweets from a specific location e.g. New York City
