#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
# This script replaces strings in an input text file.                         #
# It uses a dictionary in .csv format as follows.                             #
#                                                                             #
#     ReplaceStringsDictionary.csv                                            #
#         red;green                                                           #
#         apples;oranges                                                      #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
import string
import os

filename = "input.txt"
file = open(filename, "rt", encoding="latin-1")
fileDictionary = open("ReplaceStringsDictionary.csv", "rt", encoding="latin-1")

dictionary = {}
for line in fileDictionary:
    line = line.strip ()
    kvp = line.split(';') # get [k]ey and [v]alue [p]air (kvp[0] is the key; kvp[1] is the value)
    if kvp[0] in dictionary:
        print ("Warning: Duplicate Key was found: " + line) # this key is a duplicate key
    else:
        dictionary.update ({kvp[0] : kvp[1]})
        
fileDictionary.close ()

s = ""
for line in file:
    for dictionaryEntry in dictionary:
        line = line.replace (dictionaryEntry, dictionary[dictionaryEntry])
    s = s + line ;        
        
file.close ()

# Backup existing file:
os.system ("copy " + filename + " " + filename + "_backup")

# Overwrite existing file:
f = open(filename, "wt", encoding="latin-1")
f.write(s)
f.close()    
        