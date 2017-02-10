import sentiment_analyzer_lib.sentiment_analyzer_config as  config
import csv
import re

#remove extra words, such as 'the' and 'and'
def optimize_tweet_text(tweet_text):
	tweet_text = tweet_text.lower()
	#remove pronouns, prepositions, conjunctions, etc
	tweet_text_return = ""
	for i in tweet_text.split():
		word_needed = True
		for x in config.UNNEEDED_WORDS:
			if re.search(r"\b" + re.escape(i.lower()) + r"\b", x.lower()):
				word_needed = False
				break
		if word_needed == True:
			tweet_text_return = tweet_text_return + i + " "
	return tweet_text_return.strip()

#get show sentiment, return a number
def get_show_sentiment(tweet_text):
	tweet_score = 0
	with open(config.SENTIMENT_DICTIONARY) as sentiment_dictionary:
		reader = csv.reader(sentiment_dictionary,delimiter=' ')
		for row in reader:
			usable_row = row[0].split(",")#convert row into a list so we can check if tweet word is in there, get the sentiment
			sentiment_word = usable_row[config.SENTIMENT_DICTIONARY_WORD]
			tweet_text_split = tweet_text.split()
			for index,word in enumerate(tweet_text_split):
				if re.search(r"\b" + re.escape(word) + r"\b", sentiment_word):
					word_score = usable_row[config.SENTIMENT_DICTIONARY_SCORE]
					for i in range(0,index):
						#get multiplier
						if config.MULTIPLIER_WORDS.has_key(tweet_text_split[i]):
							word_score *= int(config.MULTIPLIER_WORDS[tweet_text_split[i]])
					tweet_score += int(word_score)
	return tweet_score

#analyze tweet, return state, show name, and sentiment score
def tweet_analyzer(tweet_data):
	try:#error control in case we get invalid states, we want to return false
		show_name = tweet_data.split("\t")[config.TWEET_NAME_COLUMN].strip()
		tweet_text = tweet_data.split("\t")[config.TWEET_TEXT_COLUMN].strip()
		tweet_state = tweet_data.split("\t")[config.TWEET_STATE_COLUMN].strip()
		if tweet_state == "" or tweet_text == "" or show_name == "":
			return False
	except IndexError:
		return False

	tweet_text = optimize_tweet_text(tweet_text)#could do one line, want it readable
	if show_name == False or tweet_state == False:
		return False
	show_sentiment = get_show_sentiment(tweet_text)
#	if show_sentiment == 0:
		#send show text to another file, so we can examine for possible addition to dictionary

	#put sentiment, show name and state into results
	return [show_name,tweet_state,show_sentiment]


