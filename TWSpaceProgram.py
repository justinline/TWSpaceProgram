'''TW Space Program, launching Rovers onto mars!'''

import sys 

from shipyard import Rover
from space import Planet

class MissionData(object):
    '''Object for Storing Mission Test Files'''
    def __init__(self, filepath):
        self.file = open(filepath, "r").readlines()

def parse_test_data(filepath):
    '''Opens and processes test file into a list of lists when called by launch()'''
    try:
        data = MissionData(filepath)    
    except IOError:
        print("Launch Test Data was not found at the specified location:", filepath)
        print("Please check file exists and try again")
        return sys.exit(1)
    data.planet = data.file[0].strip('\n').split(' ')
    f = data.file[1:]
    data.rovers = [(f[i].strip('\n').split(' '),f[i+1].strip('\n')) for i in range(0,len(f),2)]
    return data

def launch(filepath):
    '''Function to start the mission! Initialises Rovers with instructions'''
    data = parse_test_data(filepath)
    planet = Planet(lat=int(data.planet[0]), lon=int(data.planet[1]))
    rovers = [Rover(landing=cmd[0], commands=cmd[1], planet=planet) for cmd in data.rovers]
    return rovers

if len(sys.argv) > 1:
    rovers = launch(sys.argv[1])
    for rover in rovers:
        rover.path()
        print(rover.report())
