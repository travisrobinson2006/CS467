import os
import sys
import time
from threading import Thread
from apscheduler.scheduler import Scheduler
import logging
import acquire_tweets.tweet_scraper as tweet_scraper
import acquire_tweets.tweet_cleaner as tweet_cleaner
import error_message_sender

#Travis Robinson
#Centaurus
#CS467
#Oregon State University

#calls on the tweet scraper
def scrape_tweets():
	print("scraping tweets...")
	tweet_scraper.tweet_scraper()

#calls on the tweet cleaner
def clean_tweets():
	print("cleaning tweets...")
	tweet_cleaner.clean_tweets()


try:#on launch clean whatever tweets are already there are uncleaned
	clean_tweets()
except:
	error_message = "Error: " + str(e)
	print(error_message)
	error_message_sender.send_error_message(error_message)	
try:
	scheduler = Scheduler()#scheduler used to set up tweet cleaning schedule
	scheduler.start()
	scheduler.add_interval_job(clean_tweets,hours=1)#clean tweets once an hour
	logging.basicConfig()
	scrape_tweets()#start scraping tweets
	while(True):#to make sure that program doesn't end making us lose the cleaner and scraper progress
		time.sleep(2)
except (KeyboardInterrupt,SystemExit):#if we make call to exit, shut down scheduler
	scheduler.shutdown()
	print("Shutting Down...")
except Exception as e:#if there's another error (some kind of system failure, or an error with cleaning or scraping, send an alert)
	scheduler.shutdown()
	error_message = "Error: " + str(e)
	print(error_message)
	error_message_sender.send_error_message(error_message)