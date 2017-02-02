import settings
import config
import os
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
        timestampFilename = config.BASE_FILE_NAME + fulltime + '.json'


	timestampFilename = os.path.abspath(os.path.join('../../',config.UNCLEANED_TWEETS_DIRECTORY,timestampFilename))#directory for unclean tweet storage
	db = dataset.connect(settings.CONNECTION_STRING)
	result = db[settings.TABLE_NAME].all()
	dataset.freeze(result, format='json', filename=timestampFilename)
