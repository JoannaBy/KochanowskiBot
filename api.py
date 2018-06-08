# -*- coding: utf-8 -*-

# tested with Python 3.4

import tweepy
import my_keys
import os
import random

# Set keys to variables. Note that they are imported from the my_keys.py file in the same folder
CONSUMER_KEY = my_keys.CONSUMER_KEY
CONSUMER_SECRET = my_keys.CONSUMER_SECRET
ACCESS_KEY = my_keys.ACCESS_KEY
ACCESS_SECRET = my_keys.ACCESS_SECRET

# Connect to API with the keys set above using the Tweepy library
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


###############
# Some things to try. Try uncommenting the lines with three hashes (###)
###############

# Print my account name

me = api.me().name
print(me)

import os
import random
from os import path

def readFile(filename):
    filehandle = open(filename)
    print(filehandle.read())
    filehandle.close()



fileDir = os.path.dirname(os.path.realpath('__file__'))
print(fileDir)

# Choose a quote to bot
# Find a random text in the collection
text_name = random.choice(os.listdir("songs"))
text_path = 'songs//' + text_name
filename = os.path.join(fileDir, str(text_path))
filename = os.path.abspath(os.path.realpath(filename))
print(filename)
text = open(filename).read()

# Find a random strophe beginning (marked with %)
strophes = text.split("%")
quote = random.choice(strophes)

if len(quote) > 280:
	lines = quote.readlines()
	quote = (lines[:3])


# Update my status

api.update_status(status=quote)

# Perform a search

# results = api.search(q="#NYCDHWeek")
# for result in results:
#     print('\n')
#     print(result.text)

# Write your search to a file (make sure the section above is uncommented)

# f = open('search.txt','w')
# for result in results:
#    f.write(result.text) 
# f.close()

