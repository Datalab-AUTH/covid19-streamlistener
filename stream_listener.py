#!/usr/bin/env python3

import tweepy
import json
import pymongo
from pymongo import MongoClient
import datetime
import sys
import os

mongoURL = os.environ['MONGOURL']
mongoDB = os.environ['MONGODB']
mongoCollection = os.environ['MONGOCOLLECTION']
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_key = os.environ['ACCESS_KEY']
access_secret = os.environ['ACCESS_SECRET']

client = MongoClient(mongoURL)
db = client[mongoDB]
coll=db[mongoCollection]

WORDS = ['#κορωνοιος',
        '#COVID19greece',
        'covid19greece',
        '#μενουμε_σπιτι',
        '#μενουμεσπιτι',
        '#κορονα',
        '#κορονοϊος',
        '#καραντινα',
        '#εοδυ',
        '#eody',
        '#απαγορευση_κυκλοφοριας',
        '#απαγορευσηκυκλοφοριας']

class StreamListener(tweepy.StreamListener):
    #This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code),
                file=sys.stderr)
        return False

    def on_data(self, data):
        # This is the meat of the script...it connects to your mongoDB
        # and stores the tweet
        try:
            datajson = json.loads(data)
            # grab the 'created_at' data from the Tweet to use for display
            # and change it to Date object
            created_at = datajson['created_at']
            text = str(datajson['text'].encode('utf8'))
            dt = datetime.datetime.strptime(created_at,
                    '%a %b %d %H:%M:%S +0000 %Y')
            datajson['created_at'] = dt
            coll.insert(datajson)
        except Exception as e:
           print(e)

def start_stream():
    while True:
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_key, access_secret)
            # Set up the listener. The 'wait_on_rate_limit=True' is needed
            # to help with Twitter API rate limiting.
            listener = StreamListener(api = tweepy.API(wait_on_rate_limit=True,
                                                wait_on_rate_limit_notify=True,
                                                compression=True))
            streamer = tweepy.Stream(auth=auth, listener=listener)
            print("Tracking: " + str(WORDS))
            streamer.filter(track=WORDS)
        except:
            continue

if __name__ == "__main__":
    start_stream()

