#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
# This script filters all duplicate lines in a text file                      #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import string

foundLines = set ()

fileRead = open("input.txt", "rt", encoding="latin-1")
fileWrite = open("output.txt", "wt", encoding="latin-1")

for line in fileRead:
    # Remove any leading whitespace characters
    lineWithoutSpaces = line.lstrip (string.whitespace)
    lineWithoutSpaces = lineWithoutSpaces.rstrip (string.whitespace)
    if lineWithoutSpaces in foundLines:
        pass # do nothing, because this line is a duplicate line
    else:
        foundLines.add (lineWithoutSpaces)
        fileWrite.write(line)
                
fileRead.close ()
fileWrite.close ()        
        