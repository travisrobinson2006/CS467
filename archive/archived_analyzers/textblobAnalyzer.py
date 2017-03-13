import dataset
from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError
import json
import time
import csv
import string


#function that takes the text from a tweet and returns its sentiment score
def textblobScore(text):
        tbText = TextBlob(text)
        return tbText.sentiment[0]

#function to remove all non-ascii characters from the tweet text
def stripNonAscii(string):
        stripped = (c for c in string if 0 < ord(c) < 127)
        return ''.join(stripped)

#specify the names of the input file to be processed and the output file to be produced.
inputfilename = "tweets_ready_for_use"
outputfilename = "textblobScores_demo"

#define columns
showCol = 0
textCol = 1
stateCol = 2

outputfile = open(outputfilename, 'w')

#loop through each tweet in the input file, get a score for it, and then
#create an output file in the format of <show_name> <state> <sentimentScore> , table delimited
with open(inputfilename, 'r') as tweetsfile:
        reader = csv.reader(tweetsfile, delimiter = '\t')
        for row in reader:
                fixedText = stripNonAscii(row[textCol])
                sentScore = textblobScore(fixedText)
                outputfile.write(row[showCol] + '\t' + row[stateCol] + '\t' + str(sentScore) + '\n')


outputfile.close()
