import string
import csv

cleanFilename = "trainingclean.txt"
file = open(cleanFilename, 'r')
reader = csv.reader(file, delimiter = '\t')

lineCount = sum(1 for row in reader)
print lineCount
#reset the readers to the beginning of the file
file.seek(0)


numBad = 0
numGood = 0

for i in range(0, lineCount-1):
        #print i
        row = next(reader)
	print row[0]
        if (int(row[0]) == 0):
                numBad += 1
        else:
		numGood += 1

print("Correct: " + str(numGood))
print("Wrong: " + str(numBad))
