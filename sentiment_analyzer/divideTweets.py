import string
import csv

inputfilename = "dataset_michTweetsClean.txt"
outputTrainFilename = "trainhalf.txt"
outputTestFilename = "testhalf.txt"

trainfile = open(outputTrainFilename, 'w')
testfile = open(outputTestFilename, 'w')

with open(inputfilename, 'r') as tweetsfile:
	reader = csv.reader(tweetsfile, delimiter = '\t')
	linecount = 0
	traincount = 0
	testcount = 0
	for row in reader:
		print "Got Here"
		if (linecount % 3 == 0) or (linecount % 3 == 1):
			traincount += 1
			trainfile.write(row[0] + '\t' + row[1] + '\n')
		else:
			testcount += 1
			testfile.write(row[0] + '\t' + row[1] + '\n')
		linecount += 1

print linecount
print traincount
print testcount

trainfile.close()
testfile.close()
