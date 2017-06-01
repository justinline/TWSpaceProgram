'''TW Space Program, launching Rovers onto mars!'''

import os # Required to read text files
import sys # Required to read command line args


def upload_data(testfile):
    '''Opens and processes test file'''
    query = os.path.isfile(testfile)
    if query == False:
        print('Could not upload launch coordinates to Rovers')
        return 1
    data = open(testfile, "r").readlines() 
    data = [line.strip('\n').split(' ') for line in data]
    # launch(data)
    return 0
    
