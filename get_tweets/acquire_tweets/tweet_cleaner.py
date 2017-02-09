import tweet_cleaner_lib.config as config
import tweet_cleaner_lib.tweet_cleaner_tools as tweet_cleaner_tools
import json
import time
import os
import string
from apscheduler.scheduler import Scheduler
import error_message_sender

#Travis Robinson
#Centaurus
#CS467
#Oregon State University

#this function handles the tweet cleaning, removes hashtags, standardizes location, places into single tab seperated file
def clean_tweets():
	print("Beginning processing for time: " + time.strftime("Y%Y-M%m-D%d-H%H"))

	unclean_tweets_directory = os.path.abspath(config.UNCLEANED_TWEETS_DIRECTORY)#directory for unclean tweet storage
	clean_tweets_directory = os.path.abspath(os.path.join(config.CLEANED_TWEETS_DIRECTORY,config.BASE_FILE_NAME_CLEAN))#directory for clean tweet storage

	try:
		with open(os.path.join(unclean_tweets_directory,config.LIST_OF_CLEANED_TWEET_FILES)) as cleaned_tweets_list:
			list_of_cleaned_tweet_files = cleaned_tweets_list.readlines()
		list_of_cleaned_tweet_files = [i.strip() for i in list_of_cleaned_tweet_files]
	except:
		print("No cleaned tweets yet")
		list_of_cleaned_tweet_files = []

	for potential_tweets_file in os.listdir(unclean_tweets_directory):
		if potential_tweets_file.startswith(config.BASE_FILE_NAME_UNCLEAN) and potential_tweets_file.endswith(".json") and potential_tweets_file not in list_of_cleaned_tweet_files:
			print("Beginning processing for file: " + potential_tweets_file)
			with open(os.path.join(unclean_tweets_directory,potential_tweets_file)) as tweets_file:
				try:
					tweets_data = json.load(tweets_file)
					tweets = tweets_data['results']
					for i in tweets:
						clean_text = tweet_cleaner_tools.tweet_text_cleaner(i['text'])#clean up tweet text
						clean_location = tweet_cleaner_tools.tweet_location_cleaner(i['user_location'])#clean tweet location
						show_name = tweet_cleaner_tools.get_show_name(clean_text.lower())
						if clean_location != False and show_name != False:#check if a valid location, dispose of if it's not
							with open(clean_tweets_directory,'a') as output:#write cleaned tweet text and location if tweet is valid
								output.write(show_name + '\t' + clean_text + '\t' + clean_location + '\n')
				except Exception as e:
					error_message = "There was an error with file " + potential_tweets_file + ": " + str(e)
					print(error_message)
					error_message_sender.send_error_message(error_message)

			with open(os.path.join(unclean_tweets_directory,config.LIST_OF_CLEANED_TWEET_FILES),'a') as cleaned_tweets_list:
				cleaned_tweets_list.write(potential_tweets_file + '\n')