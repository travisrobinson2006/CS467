import settings
import tweepy
import dataset
import time
from textblob import TextBlob

def dumpjson():
	day = time.localtime(time.time())[7]
        hour = time.localtime(time.time())[3]
        minute = time.localtime(time.time())[4]
        fulltime = str(day) + '-' + str(hour) + '-'+ str(minute)
        print fulltime
        timestampFilename = 'tweets' + fulltime + '.json'

	db = dataset.connect(settings.CONNECTION_STRING)
	result = db[settings.TABLE_NAME].all()
	dataset.freeze(result, format='json', filename=timestampFilename)
