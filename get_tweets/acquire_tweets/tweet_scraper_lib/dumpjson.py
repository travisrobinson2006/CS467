import settings
import tweepy
import dataset
import time
from textblob import TextBlob

def dumpjson():
	print("Dumping Tweets to JSON")
	day = time.localtime(time.time())[7]
        hour = time.localtime(time.time())[3]
        minute = time.localtime(time.time())[4]
        fulltime = str(day) + '-' + str(hour) + '-'+ str(minute)
        print fulltime
        timestampFilename = 'acquire_tweets/unclean_tweets/tweets' + fulltime + '.json'

	db = dataset.connect(settings.TEMP_CONNECTION_STRING)
	result = db[settings.TABLE_NAME].all()
	print(db[settings.TABLE_NAME].count())
	dataset.freeze(result, format='json', filename=timestampFilename)
	db[settings.TABLE_NAME].delete()