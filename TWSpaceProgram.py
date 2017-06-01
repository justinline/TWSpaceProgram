'''TW Space Program, launching Rovers onto mars!'''

import os # Required to read text files
import sys # Required to read command line args

from shipyard import Rover

def upload_data(testfile):
    '''Opens and processes test file when called by launch()'''
    query = os.path.isfile(testfile)
    if query == False:
        raise ValueError
    data = open(testfile, "r").readlines() 
    data = [line.strip('\n').split(' ') for line in data]
    return data

def launch(testfile):
    '''Function to start the mission! Initialises Rovers with instructions'''
    try:
        data = upload_data(testfile)
    except ValueError:
        print('Failed launch, Bad Data. Please format text file correctly.')
        return 1
    planet = data.pop(0)
    rovers = []
    for i in range(int(len(data) / 2)):
        rovers.append(Rover(landing=data[i * 2], commands=data[(i * 2) + 1]))
    return rovers
