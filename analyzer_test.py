import sentiment_analyzer_working_title as analyzer
from random import randint


with open("scored_tweets_testing") as tweets:
	counter = 0
	correct_answer = 0
	incorrect_answer = 0
	total_questions = 0
	tweets = tweets.readlines()
	for i in tweets:
		counter += 1
		tweet_text = i.split("\t")[1]
		try:
			score = i.split("\t")[3]
			total_questions += 1
			if analyzer.tweet_analyzer(tweet_text) == int(score):
				correct_answer += 1
			else:
				incorrect_answer += 1
		except:
			print("No Score: Skipping Test #" + str(counter))

	print("Out of " + str(total_questions) + " there were " + str(correct_answer) + " correct answers and " + str(incorrect_answer) + " incorrect answers")


#		print(tweets[i])
#		print(analyzer.tweet_analyzer(tweets[i]))
#		analyzer.tweet_analyzer(tweets[index])
