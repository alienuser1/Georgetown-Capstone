from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.GtownTwitter_PROD
print ', '.join(db.collection_names())
#
#
def pretty_print_flat_object(obj):
    max_key_width = max(len(field) for field in obj.iterkeys())
    for field in tweet.iterkeys():
        print "{:>{width}}: {}".format(field, tweet[field], width=max_key_width)
tweet = db.friendships_collection.find_one()        
pretty_print_flat_object(tweet)
#
#
print 'The total number of tweets in the dtabase is: '
db.friendships_collection.count()
#db.tweets_collection.count()
