#Imports
import pandas as pd
import tweepy
from tweepy import api
import datetime
import time
from datetime import timedelta
import tweepy.error
import csv
import json
from tweepy.error import RateLimitError
from tweepy.error import TweepError
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
import random
import time
import datetime
from datetime import timedelta

#######################################################################################
#Merge all files
#Merge all files
ids = {}
path = 'liste1.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()
path = 'liste2.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()
path = 'liste3.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()
path = 'liste4.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()
path = 'liste5.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()
path = 'liste6.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()
path = 'liste7.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()
path = 'liste8.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()
path = 'liste9.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()
path = 'liste10.txt'
with open(path, 'r') as fp:
    ids.update(json.load(fp))
    fp.close()

print(len(ids))

######################################################################################
#Methods
def getFriends(cursor):
    try:
        for page in cursor.pages():
            yield page
        
    except tweepy.TweepError as e:
        print(e.reason)
        getFriends(cursor)
        
#####################################################################################

#Retrieve ids
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')
api = tweepy.API(auth)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, timeout=10)
  
friends_ids = {}
for iid in ids:
    print(iid)
    friends_ids[iid] = []
    try:
        c = tweepy.Cursor(api.friends_ids, id = iid)
        for page in c.pages():
            friends_ids[iid] += page
    except TweepError:
        print('tweeperror')
        continue
    with open('friends_ids.txt', 'w+') as fp:
        json.dump(friends_ids, fp)