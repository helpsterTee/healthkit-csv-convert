#!/usr/bin/python
import sys

# variables to watch - change this as needed, e.g. ["type1", "type2", "..."]
types = ["HKQuantityTypeIdentifierHeartRate"]
field_separator = ";"
line_separator = "\n"


### DO NOT CHANGE ANYTHING BELOW THIS LINE
if (len(sys.argv) <= 2):
    print("Usage: ./extractHeartRate.py imput.xml output.csv\n")
    quit()

fileIn = open(sys.argv[1],'r')
fileOut = open(sys.argv[2],'w')

# init header
typedesc = "Date"
for t in types:
    typedesc += field_separator+t
typedesc += line_separator
fileOut.write(typedesc)

# parse lines
for line in fileIn:
    for t in types:
        found = line.find(t, 0, len(line))
        if found != -1:
            #date
            extractDateBegin = line.find("creationDate", 0, len(line))
            extractDateBegin = line.find("\"", extractDateBegin, len(line))
            extractDateEnd = line.find("\"",extractDateBegin+1, len(line))

            # value
            extractBegin = line.find("value", 0, len(line))
            extractBegin = line.find("\"", extractBegin, len(line))
            extractEnd = line.find("\"",extractBegin+1, len(line))

            # write out result
            fileOut.write(line[extractDateBegin+1:extractDateEnd]+field_separator+line[extractBegin+1:extractEnd]+line_separator)
fileIn.close()
