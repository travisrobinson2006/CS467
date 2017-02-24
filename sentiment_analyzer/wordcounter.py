#a nice python class that lets you count how many times items occur in a list
from collections import Counter
import csv
import re
import string
import sentiment_analyzer_lib.settings as settings


sentCol = 0
textCol = 1

# Read in the training data.
with open("trainhalf.txt", 'r') as file:
  reviews = list(csv.reader(file, delimiter = '\t'))

def get_text(reviews, score):
  # Join together the text in the reviews for a particular tone.
  # We lowercase to avoid "Not" and "not" being seen as different words, for example.
  return " ".join([r[textCol].lower() for r in reviews if r[sentCol] == str(score)])

def count_text(text):
  # Split text into words based on whitespace.  Simple but effective.
  words = re.split("\s+", text)
  # Count up the occurence of each word.
  return Counter(words)

negative_text = get_text(reviews, -1)
positive_text = get_text(reviews, 1)
# Generate word counts for negative tone.
negative_counts = count_text(negative_text)
# Generate word counts for positive tone.
positive_counts = count_text(positive_text)




###############################################################




def get_y_count(score):
  # Compute the count of each classification occuring in the data.
  return len([r for r in reviews if r[sentCol] == str(score)])

# We need these counts to use for smoothing when computing the prediction.
positive_review_count = get_y_count(1)
negative_review_count = get_y_count(-1)
print("positive_review_count = " + str(positive_review_count))
print("negative_review_count = " + str(negative_review_count))
print("len(reviews) = " + str(len(reviews)))

# These are the class probabilities (we saw them in the formula as P(y)).
prob_positive = float(positive_review_count) / float(len(reviews))
prob_negative = float(negative_review_count) / float(len(reviews))


def make_class_prediction(text, counts, class_prob, class_count):
	prediction = 1
	text_counts = Counter(re.split("\s+", text))
	for word in text_counts:

	#For every word in the text, we get the number of times that word occured in the reviews for a given class, 
	# add 1 to smooth the value, and divide by the total number of words in the class (plus the class_count to also smooth the denominator).
	#Smoothing ensures that we don't multiply the prediction by 0 if the word didn't exist in the training data.
	#We also smooth the denominator counts to keep things even.
		numerator = text_counts.get(word) * (counts.get(word, 0) + 1)
		denomenator = sum(counts.values()) + class_count
		
		prediction *= float(numerator) / float(denomenator)
	#Now we multiply by the probability of the class existing in the documents.	
	return prediction * class_prob

def make_decision(text, make_class_prediction):
	#Compute negative and positive probabilities
	neg_prob = make_class_prediction(text, negative_counts, prob_negative, negative_review_count)
	pos_prob = make_class_prediction(text, positive_counts, prob_positive, positive_review_count)
	if neg_prob > pos_prob:
		#print "Case 1"
		#print("neg_prob = " + str(neg_prob))
		#print("pos_prob = " + str(pos_prob))
		compScore = (neg_prob - pos_prob) / float(neg_prob + pos_prob)
		compScore = -1.0*round(compScore, 3)
		return [-1, compScore]
	else:
		compScore = (pos_prob - neg_prob) / float(neg_prob + pos_prob)
		compScore = round(compScore, 3)
		return [1, compScore]

def stripNonAscii(string):
        stripped = (c for c in string if 0 < ord(c) < 127)
        return ''.join(stripped)



# As you can see, we can now generate probabilities for which class a given review is part of.
# The probabilities themselves aren't very useful -- we make our classification decision based on which value is greater.
#print("Review: {0}".format(testText))
#print("Negative prediction: {0}".format(make_class_prediction(testText, negative_counts, prob_negative, negative_review_count)))
#print("Positive prediction: {0}".format(make_class_prediction(testText, positive_counts, prob_positive, positive_review_count)))

#specify the names of the input file to be processed and the output file to be produced.
inputfilename = "testhalf.txt"
outputfilename = "nbScoresWithText.txt"

outputfile = open(outputfilename, 'w')

#loop through each tweet in the input file, get a score for it, and then
#create an output file in the format of <show_name> <state> <sentimentScore> , table delimited
with open(inputfilename, 'r') as tweetsfile:
        reader = csv.reader(tweetsfile, delimiter = '\t')
        for row in reader:
                fixedText = stripNonAscii(row[1])
		fixedText = str.lower(fixedText)
		for content in settings.TRACK_TERMS:
			fixedText = fixedText.replace(content, "")	
		sentScoreResults = make_decision(fixedText, make_class_prediction)
		binaryScore = sentScoreResults[0]
		compScore = sentScoreResults[1]
		 
                outputfile.write(str(binaryScore) + "\t" + fixedText + '\n')


outputfile.close()
