import sentiment_analyzer_working_title as analyzer

TEST_TERMS = [
"Breaking Bad. I'm at the very end of the series and its basically just one big shit fest 	OH",
"I love law and order svu, never gets old ... 	LA",
]

for i in TEST_TERMS:
	analyzer.tweet_analyzer(i)
