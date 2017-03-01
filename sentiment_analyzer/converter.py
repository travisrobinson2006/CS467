import string
import csv

inputFilename = "textblobScores.txt"
inScoreCol = 2
outputFilename = "textblobScoresForTesting.txt"
output = open(outputFilename, 'w')

with open(inputFilename, 'r') as input:
	reader = csv.reader(input, delimiter = '\t')
	for row in reader:
		if (float(row[inScoreCol]) < 0.0):
			output.write("-1" + '\n')
		else:
			output.write("1" + '\n')

output.close()

