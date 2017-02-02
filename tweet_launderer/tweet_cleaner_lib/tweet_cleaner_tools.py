import config

def tweet_text_cleaner(tweet_text):
	tweet_text = tweet_text.encode("utf-8") #utf-8 encoding used so tweet text can be properly read (twitter uses utf-8)
	cleaned_tweet_text = "" #start empty string, will fill with cleaned string
	for word in tweet_text.split(): #iterate through each word, removing hashtags and tagged people
		if word[0] not in config.SYMBOLS_TO_DROP and not word.startswith('https'):
			cleaned_tweet_text = cleaned_tweet_text + word + ' '		
	return cleaned_tweet_text

def tweet_location_cleaner(tweet_location):
	if tweet_location is not None:#don't have a null value for user location
		tweet_location = tweet_location.encode("utf-8").strip()#use usable charset, strip leading/trailing white space
		if len(tweet_location.split()) == 1:#if location only single word, check if it's a valid state
			return valid_state_checker(tweet_location)
		elif len(tweet_location.split()) > 1:#if more than 1 word, need to check for location formatting
			last_word = tweet_location.split()[len(tweet_location.split())-1]#split off last word
			if last_word.upper() in config.COUNTRY_ABBREVIATIONS.keys() or last_word.upper() in config.COUNTRY_ABBREVIATIONS.values():#check if last word is US
				potential_state = tweet_location.split()[len(tweet_location.split())-2]#if the last word is the US, see if a valid state is provided
				valid_state_checker(potential_state)
			else:#if last word is not US see if it's a valid state
				return valid_state_checker(last_word)
		else:
			raise TypeError('ERROR: THIS CODE SHOULD NOT BE EXECUTED: TWEET_LOCATION_CLEANER: TWEET LOCATION HAD LENGTH 0 BUT WAS NOT OF TYPE NONE')
	else:#have a null value for user location
		return False


def valid_state_checker(tweet_location):
	if tweet_location.upper() in config.STATE_ABBREVIATIONS.keys():#see if location in keys
		return config.STATE_ABBREVIATIONS[tweet_location.upper()]
	elif tweet_location.upper() in config.STATE_ABBREVIATIONS.values():#see if location in values
		return tweet_location.upper()
	else:#if location not in either, bad location, return false
		return False	