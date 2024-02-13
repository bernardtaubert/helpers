#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
# This script removes silence from a .wav file by using pydub.                #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
import os
import re
import sys
sys.path.insert(0,'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\ffmpeg-4.2-win32-static\\bin')

from pydub import AudioSegment
from pydub.playback import play

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    # sound is a pydub.AudioSegment
    # silence_threshold in dB
    # chunk_size in ms
    #iterate over chunks until you find the first one with sound
    
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms

def trim_wav(filename):  
    sound = AudioSegment.from_file(filename, format="wav")

    start_trim = detect_leading_silence(sound, -78.7)
    end_trim = detect_leading_silence(sound.reverse(), -78.7)

    duration = len(sound)    
    trimmed_sound = sound[start_trim:duration-end_trim]
    trimmed_sound.export(filename) #overwrites existing file
    
def findfiles(filepattern, base = '.', search_recursively = ''):
    #Find files matching a regex pattern recursively in base
    regex = re.compile(filepattern)
    matches = []
    if (search_recursively == '-r'):
        for root, dirs, files in os.walk(base):
            for singlefile in files:
                if regex.match(singlefile):
                    matches.append(root + '\\' + singlefile)
    else:
        for singlefile in os.listdir():
            if os.path.isfile(singlefile) and regex.match(singlefile):
                matches.append(singlefile)
    return matches
 
allfiles = findfiles(r".*\.wav", '.', '-r') # recursively search for the files

for file in allfiles:
    print (file)
    trim_wav(file)    
