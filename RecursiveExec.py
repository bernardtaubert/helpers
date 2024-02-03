#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
# This script runs an executable for all files that have been found in a      #
# directory tree, that match the extension filepattern (txt).                 #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
import os
from glob import glob

filepaths = [y for x in os.walk('.') for y in glob(os.path.join(x[0], '*.txt'))]

for file in filepaths:
  print ("Execute " + file)
  os.system("MyExeFile.exe " + file)