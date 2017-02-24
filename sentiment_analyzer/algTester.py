import string
import csv


algResultsFilename = "nbScoresWithText.txt"
actualSentScoresFilename = "testhalf.txt"

scoreCol = 0
textCol = 1

results = open(algResultsFilename, 'r')
actual = open(actualSentScoresFilename, 'r')
resultsReader = csv.reader(results, delimiter = '\t')
actualReader = csv.reader(actual, delimiter = '\t')

resultsLineCount = sum(1 for row in resultsReader)
actualLineCount = sum(1 for row in actualReader)
print resultsLineCount
print actualLineCount
lineCount = actualLineCount
#reset the readers to the beginning of the file
results.seek(0)
actual.seek(0)

numCorrect = 0
numWrong = 0
for i in range(0, lineCount-1):
	#print i
	resultsRow = next(resultsReader)
	actualRow = next(actualReader)
	
	if (resultsRow[scoreCol] == actualRow[scoreCol]):
		numCorrect += 1
	else:
		numWrong += 1


percentCorrect = (numCorrect/float(numCorrect+numWrong))*100.0
print("Correct: " + str(numCorrect))
print("Wrong: " + str(numWrong))
print("Percent Correct: " + str(percentCorrect))

