import sentiment_analyzer_working_title as analyzer

TEST_TERMS = [
"the bachelor	Finally watched yesterday's episode of the bachelor and so happy with who went home 	CA",
"the bachelor	Trump's treating it more like \"The Bachelor\". I expect him to hand out a rose 	TX]"
]

with open("sample_tweets.txt") as tweets:
	tweets = tweets.readlines()
	for i in tweets:
		print(analyzer.tweet_analyzer(i))

tweetfile = open("sample_tweets.txt", "r")

tweetlist = []
for line in tweetfile:
	tweetlist.append(line)

for i in tweetlist:
#	print i
	print(analyzer.tweet_analyzer(i))

#for i in TEST_TERMS:
#	print(analyzer.tweet_analyzer(i))
#	analyzer.tweet_analyzer(i)



#	print(tweets)

#for i in TEST_TERMS:
#	print(analyzer.tweet_analyzer(i))
#	analyzer.tweet_analyzer(i)