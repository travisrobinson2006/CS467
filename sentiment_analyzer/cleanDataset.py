import dataset
from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError
import json
import time
import csv
import string
import re

#function that takes the text from a tweet and returns its sentiment score
def textblobScore(text):
        tbText = TextBlob(text)
        return tbText.sentiment[0]

#function to remove all non-ascii characters from the tweet text
def stripNonAscii(string):
        stripped = (c for c in string if 0 < ord(c) < 127)
        return ''.join(stripped)

#specify the names of the input file to be processed and the output file to be produced.
inputfilename = "dataset_genericTweets.txt"
outputfilename = "dataset_genericTweetsClean.txt"

#define columns
sentCol = 0
textCol = 1

#define what the dataset uses for a positive score and negative score
oldPosScore = 1
oldNegScore = -1

#The training file is tweets about a handful of titles. The content names will be removed
#from the tweets before word counts are formed. Below is a list of those titles.
titleNames = ["the da vinci code",
"da vinci code",
"da vinci",
"mission impossible 3",
"mission impossible III",
"mission impossible",
"harry potter",
"brokeback mountain"]

outputfiletemp = open("temp.txt", 'w')
outputfile = open(outputfilename, 'w')

#loop through each tweet in the input file, get a score for it, and then
#create an output file in the format of <show_name> <state> <sentimentScore> , table delimited
with open(inputfilename, 'r') as tweetsfile:
        reader = csv.reader(tweetsfile, delimiter = '\t')
        for row in reader:
                fixedText = stripNonAscii(row[textCol])
		fixedText = str.lower(fixedText)
		for content in titleNames:
			#print content
			#fixedText = re.sub(content, '', fixedText)
			fixedText = fixedText.replace(content, "")
                
		if (int(row[sentCol]) == oldPosScore):
                        outputfiletemp.write(str(1) + '\t' + fixedText + '\n')
                if (int(row[sentCol]) == oldNegScore):
                        outputfiletemp.write(str(-1) + '\t' + fixedText + '\n')
outputfiletemp.close()	
		
with open("temp.txt", 'r') as tempfile:
	reader = csv.reader(tempfile, delimiter = '\t')
	for row in reader:
		if (int(row[0]) == 0):
			j = 10 #dummy statement
        	else:
                	outputfile.write(row[0] + '\t' + row[1] + '\n')

outputfile.close()
