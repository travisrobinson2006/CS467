import sentiment_analyzer_working_title as analyzer
from random import randint


with open("tweets_ready_for_use") as tweets:
	tweets = tweets.readlines()
	for i in range(0,30):
		index = randint(0,len(tweets))
#		print(tweets[i])
#		print(analyzer.tweet_analyzer(tweets[i]))
		analyzer.tweet_analyzer(tweets[index])
