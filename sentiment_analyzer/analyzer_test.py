import sentiment_analyzer_working_title as analyzer

TEST_TERMS = [
"breaking bad 	Breaking Bad. I'm at the very end of the series and its basically just one big shit fest 	OH",
"law and order svu 	I love law and order svu, never gets old ... 	LA",
]

for i in TEST_TERMS:
	print(analyzer.tweet_analyzer(i))
