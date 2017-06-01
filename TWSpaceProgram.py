'''TW Space Program, launching Rovers onto mars!'''

import os 
import sys 

from shipyard import Rover
from space import Planet


def upload_data(testfile):
    '''Opens and processes test file when called by launch()'''
    query = os.path.isfile(testfile)
    if query == False:
        #TODO: Make this check more robust
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
    target = data.pop(0)
    planet = Planet(lat=int(target[0]), lon=int(target[1]))
    rovers = []
    for i in range(int(len(data) / 2)):
        rovers.append(Rover(landing=data[i * 2], commands=data[(i * 2) + 1], planet=planet))
    return rovers
