#import sentiment_analyzer_working_title as analyzer
import sentiment_analyzer_lib.sentiment_analyzer_config as  config
import re
import ast
from random import randint

def optimize_tweet_text(tweet_text,show_name):
	tweet_text = tweet_text.lower()
	tweet_text = re.sub("[^a-zA-Z0-9-_']"," ", tweet_text)#remove other chars, ie emojis
	tweet_text = tweet_text.replace(show_name,"")#remove show name, want only text for sentiment analysis
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



with open("tweets_ready_for_use") as tweets:
	tweets = tweets.readlines()
	
	try:
		with open ('pos_words','r') as pos_words:
			pos_words_dict = ast.literal_eval(pos_words.read())
	except IOError:
		pos_words_dict = {}

	try:
		with open ('neg_words','r') as neg_words:
			neg_words_dict = ast.literal_eval(neg_words.read())
	except IOError:
		neg_words_dict = {}

#	if not isinstance(pos_words_dict,dict):
#		pos_words_dict = {}
#	if not isinstance(neg_words_dict,dict):
#		neg_words_dict = {}


	for i in range(0,30):
		index = randint(0,len(tweets))
		show_name = tweets[index].split("\t")[config.TWEET_NAME_COLUMN].strip()
		tweet_text = tweets[index].split("\t")[config.TWEET_TEXT_COLUMN].strip()
		tweet_state = tweets[index].split("\t")[config.TWEET_STATE_COLUMN].strip()

		print("\n" + tweet_text)
		score = int(input("Select -1 for negative tweet, 0 for neutral, or 1 for positive: "))
		while score not in [-1,0,1]:
			score = int(input("Invalid. Select -1 for negative tweet, 0 for neutral, or 1 for positive: "))				

		tweet_text = optimize_tweet_text(tweet_text,show_name)
		if score == 1:
			for i in tweet_text.split():
				if i in pos_words_dict.keys():
					pos_words_dict[i] += 1
				else:
					pos_words_dict[i] = 1
		if score == -1:
			for i in tweet_text.split():
				if i in neg_words_dict.keys():
					neg_words_dict[i] += 1
				else:
					neg_words_dict[i] = 1

with open('pos_words','w') as pos_words:
	pos_words.write(str(pos_words_dict))
with open('neg_words','w') as neg_words:
	neg_words.write(str(neg_words_dict))
