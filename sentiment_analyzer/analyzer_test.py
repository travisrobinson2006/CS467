import sentiment_analyzer_working_title as analyzer

with open("sample_tweets.txt") as tweets:
	tweets = tweets.readlines()
	for i in tweets:
#		print(analyzer.tweet_analyzer(i))
		analyzer.tweet_analyzer(i)
