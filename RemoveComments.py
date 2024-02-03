#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
# This script removes comments of .c and .h files.                            #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
import os
import re
import enum
import string

class ParseFileState(enum.Enum):
    inRoot = 0
    inSingleLineComment = 1
    inMultiLineComment = 2
     
filename = "main.c"
file = open(filename, "rt", encoding="latin-1") 
       
c = "\0" # the character that will be read from the fileRead
buffer = []
tempBuffer = [] # tempBuffer is used to accumulate all characters in every #pragma line, BUT comments like // and /* */ are skipped
state = ParseFileState.inRoot

while ("" != c):
    c = file.read(1) # read the next Character c #read = fileRead.read() # read the complete file (till the end)
    
    if state == ParseFileState.inRoot:
        tempBuffer.append (c)
        if '/' == c:
            c = file.read(1) # read the next Character c
            if '*' == c:
                state = ParseFileState.inMultiLineComment
                tempBuffer.pop () # remove the last character, because it was the start of the comment
            elif '/' == c:
                state = ParseFileState.inSingleLineComment
                tempBuffer.pop () # remove the last character, because it was the start of the comment
            else:
                tempBuffer.append (c) # append the character, because it was NOT the start of a comment
    elif state == ParseFileState.inSingleLineComment:
        if '\n' == c: 
            # reached the end of the single line comment
            tempBuffer.append (c) # append a newline character '\n' after the SingleLine Comment
            state = ParseFileState.inRoot
    elif state == ParseFileState.inMultiLineComment:
        if '*' == c:
            c = file.read(1) # read the next Character c
            if '/' == c:
                # reached the end of the multi line comment
                state = ParseFileState.inRoot
            else:
                pass # do nothing, because the program is still inside of a multi-line comment
        
file.close()

file = open(filename + "_new", "wt", encoding="latin-1")

for character in tempBuffer:
    file.write(character)

