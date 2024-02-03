#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
# This script adds incrementing numbers to a specific string                  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import string

filename = "output.txt"

# Write to file:
f = open(filename, "wt", encoding="latin-1")

for i in range(1, 218, 1): 
    f.write ("% F" + str(i) + " - List\n")
    f.write ("ListEntry(" + str(i) + ").ListElement = uint8(0);\n")    
    f.write ("ListEntry(" + str(i) + ").Array(1).lolim = uint16(0);\n")
    f.write ("ListEntry(" + str(i) + ").Array(1).uplim = uint16(0);\n")
    f.write ("ListEntry(" + str(i) + ").Array(2).lolim = uint16(0);\n")
    f.write ("ListEntry(" + str(i) + ").Array(2).uplim = uint16(0);\n")
    f.write ("ListEntry(" + str(i) + ").Array(3).lolim = uint16(0);\n")
    f.write ("ListEntry(" + str(i) + ").Array(3).uplim = uint16(0);\n")

f.close()
