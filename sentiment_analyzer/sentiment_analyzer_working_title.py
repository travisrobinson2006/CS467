import sentiment_analyzer_lib.sentiment_analyzer_config as  config
import csv
import re
import pandas
import ast


#remove extra words, such as 'the' and 'and'
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

#get show sentiment, return a number
def get_show_sentiment(tweet_text):
	tweet_score = 0
	with open ('pos_words','r') as pos_words:
		pos_words_dict = ast.literal_eval(pos_words.read())
	with open ('neg_words','r') as neg_words:
		neg_words_dict = ast.literal_eval(neg_words.read())

	words_in_pos_dict = 0
	words_in_neg_dict = 0
	total_words = 0

#	print(tweet_text)
#	tweet_text = tweet_text.split()
#	print(tweet_text)

#	counter = 0
	split_text = tweet_text.split()
	for i in split_text:
#		total_words = total_words + 1
		total_words += 1
		if i in pos_words_dict.keys():
			words_in_pos_dict += 1
		if i in neg_words_dict.keys():
			words_in_neg_dict += 1		

	try:
		pos_score = float(words_in_pos_dict) / float(total_words)
		neg_score = float(words_in_neg_dict) / float(total_words)
	except ZeroDivisionError:
		return 0
#	print(pos_score)
#	print(neg_score)

	if pos_score > neg_score and pos_score > .5:
		return 1
	elif neg_score > pos_score and neg_score > .5:
		return -1
	else:
		return 0

"""
	for i in tweet_text.split():
		if i in pos_words_dict.keys():
			tweet_score += pos_words_dict[i]
		if i in neg_words_dict.keys():
			tweet_score -= neg_words_dict[i]

	if tweet_score > 0:
		tweet_score = 1
		for i in tweet_text.split():
			if i in pos_words_dict.keys():
				pos_words_dict[i] += 1
			else:
				pos_words_dict[i] = 1
			with open('pos_words','w') as pos_words:
				pos_words.write(str(pos_words_dict))
	elif tweet_score < 0:
		tweet_score = -1
		if i in neg_words_dict.keys():
			neg_words_dict[i] += 1
		else:
			neg_words_dict[i] = 1
		with open('neg_words','w') as neg_words:
			neg_words.write(str(neg_words_dict))
"""	
#	return tweet_score

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

	if show_name == False or tweet_state == False:
		return False
	original_tweet_text = tweet_text
	tweet_text = optimize_tweet_text(tweet_text,show_name)#could do one line, want it readable
	show_sentiment = get_show_sentiment(tweet_text)

	#put sentiment, show name and state into results
	results = [(show_name,tweet_state,show_sentiment)]
	data = pandas.DataFrame.from_records(results,columns=config.COLUMN_LABELS)
	print("Text:\n" + original_tweet_text + "\nScore:\n" + str(show_sentiment))
	#return data#will remove when ready to send data to database instead
	return show_sentiment