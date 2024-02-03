#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
# This script replaces hex values by decimal values.                          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
import os
import string
import re

regExpValue = re.compile (r".*hex2dec\('([A-F0-9]+).*")
allfolders = os.listdir("../../")

for folder in allfolders:
  if folder.find("TargetDirectoryName") != -1:
    allfiles = os.listdir("../../" + folder)
    for file in allfiles:    
        if file.find("TargetFilename.txt") != -1:
          fileRead = open("../../" + folder + "/" + file, "rt", encoding="latin-1")
          content = fileRead.read() #read = fileRead.read() # read the complete file (till the end)
          lineIterator = iter(content.splitlines())
          overWriteFile = False
          tempContent = ""
          for line in lineIterator:
             if line.find ("hex2dec(") != -1:
                match = re.match (regExpValue.pattern, line, re.IGNORECASE | re.DOTALL )
                if match: # Regular Expression has matched
                   matchGroup1 = match.expand (r"\g<1>")
                   decimal = int(matchGroup1, 16)
                   print ("Converting " + matchGroup1 + " to " + str(decimal))
                   overWriteFile = True # overwrite file now
                   replacedString = line.replace("hex2dec(", str(decimal)).replace(")","")
                   splittedString = replacedString.split("'")
                   print (splittedString[0] + splittedString[2])
                   tempContent += splittedString[0] + splittedString[2] + "\n"
             else:
                tempContent += line + "\n"

          if overWriteFile == True:
            print (tempContent + "\n")
            fileRead.close()
            fileWrite = open("../../" + folder + "/" + file, "wt", encoding="latin-1")
            fileWrite.write(tempContent)
            fileWrite.close()

input()