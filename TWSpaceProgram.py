'''TW Space Program, launching Rovers onto mars!'''

import sys 

from shipyard import Rover
from space import Planet


def upload_data(filepath):
    '''Opens and processes test file into a list of lists when called by launch()'''
    try:
        data = open(filepath, "r").readlines() 
    except IOError:
        print("Launch Test Data was not found at the specified location:", filepath)
        print("Please check file exists and try again")
        return sys.exit(1)
    data = [line.strip('\n').split(' ') for line in data]
    return data

def launch(filepath):
    '''Function to start the mission! Initialises Rovers with instructions'''
    data = upload_data(filepath)
    target = data.pop(0)
    planet = Planet(lat=int(target[0]), lon=int(target[1]))
    rovers = []
    for i in range(int(len(data) / 2)):
        rovers.append(Rover(landing=data[i * 2], commands=data[(i * 2) + 1], planet=planet))
    return rovers

if len(sys.argv) > 1:
    rovers = launch(sys.argv[1])
    for rover in rovers:
        rover.path()
        print(rover.report())
