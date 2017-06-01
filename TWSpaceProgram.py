'''TW Space Program, launching Rovers onto mars!'''

import os # Required to read text files
import sys # Required to read command line args


def upload_data(testfile):
    '''Opens and processes test file'''
    query = os.path.isfile(testfile)
    if query == False:
        raise ValueError
    data = open(testfile, "r").readlines() 
    data = [line.strip('\n').split(' ') for line in data]
    return data
    
def launch(testfile):
    try:
        data = upload_data(testfile)
    except ValueError:
        print('Failed launch, Bad Data. Please format text file correctly.')
        return 1
    landing = data.pop(0)
    x, y = landing[0], landing[1]
    rovers = [Rover() for i in range(int(len(data) / 2))]
    return rovers

class Rover(object):

    def __init__(self):
        pass

    def move(self):
        pass
    
    def rotate(self):
        pass

    pass