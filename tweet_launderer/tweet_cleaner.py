import tweet_cleaner_lib.config as config
import tweet_cleaner_lib.tweet_cleaner_tools as tweet_cleaner_tools
import json
import time
import os
import string
#from apscheduler.scheduler import Scheduler


print("Beginning processing for time: " + time.strftime("Y%Y-M%m-D%d-H%H"))

#os.chdir(config.UNCLEANED_TWEETS_DIRECTORY)#directory for unclean tweets
unclean_tweets_directory = os.path.abspath(os.path.join('../',config.UNCLEANED_TWEETS_DIRECTORY))#directory for unclean tweet storage
clean_tweets_directory = os.path.abspath(os.path.join('../',config.CLEANED_TWEETS_DIRECTORY,config.BASE_FILE_NAME_CLEAN))#directory for clean tweet storage

for potential_tweets_file in os.listdir(unclean_tweets_directory):
	if potential_tweets_file.startswith(config.BASE_FILE_NAME_UNCLEAN) and potential_tweets_file.endswith(".json"):
		print("Beginning processing for file: " + potential_tweets_file)
		with open(os.path.join(unclean_tweets_directory,potential_tweets_file)) as tweets_file:
			try:
				tweets_data = json.load(tweets_file)
				tweets = tweets_data['results']
				for i in tweets:
					clean_text = tweet_cleaner_tools.tweet_text_cleaner(i['text'])#clean up tweet text
					clean_location = tweet_cleaner_tools.tweet_location_cleaner(i['user_location'])#clean tweet location
					if clean_location != False:#check if a valid location, dispose of if it's not
						with open(clean_tweets_directory,'a') as output:#write cleaned tweet text and location if tweet is valid
							output.write(clean_text + '\t' + clean_location + '\n')
			except Exception as e:
				print("There was an error with file " + potential_tweets_file + ": " + str(e))