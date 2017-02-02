import tweet_cleaner_lib.config as config
import tweet_cleaner_lib.tweet_cleaner_tools as tweet_cleaner_tools
import json
import time
import glob
import os
import string
#from apscheduler.scheduler import Scheduler


print("Beginning processing for time: " + time.strftime("Y%Y-M%m-D%d-H%H"))

os.chdir(config.NON_CLEANED_TWEETS_DIRECTORY)
for potential_tweets_file in glob.glob("*.json"):
	if potential_tweets_file.startswith(config.BASE_FILE_NAME_UNCLEAN):
		print("Beginning processing for file: " + potential_tweets_file)
		with open(potential_tweets_file) as tweets_file:
			try:
				tweets_data = json.load(tweets_file)
				tweets = tweets_data['results']
				for i in tweets:
					clean_text = tweet_cleaner_tools.tweet_text_cleaner(i['text'])#clean up tweet text
					clean_location = tweet_cleaner_tools.tweet_location_cleaner(i['user_location'])#clean tweet location
					if clean_location != False:#check if a valid location, dispose of if it's not
						print(clean_location)
					else:
						print("bad tweet")
					#if a good language validator can be found, we should insert it here, else do nothing at this point
					#print to proper file

			except Exception as e:
				print("There was an error with file " + potential_tweets_file + ": " + str(e))


clean_tweets_directory = os.path.abspath('../' + config.CLEANED_TWEETS_DIRECTORY)
output = open(os.path.join(clean_tweets_directory,config.BASE_FILE_NAME_CLEAN),'a')
output.write("well hello there")
output.close()

#with open(clean_tweets_directory,'r') as output:#permission errors on windows testing environment
#	output.write("well hello there")
