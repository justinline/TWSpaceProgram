'''TW Space Program, launching Rovers onto mars!'''

import sys 

from shipyard import Rover
from space import Planet

class MissionData(object):
    '''Object for Storing Mission Test Files'''
    def __init__(self, filepath):
        self.lines = open(filepath, "r").readlines()

def clean(line, split=False):
    line = line.strip('\n')
    if split == True:
        line = line.split(' ')
    return line

def parse_test_data(filepath):
    '''Opens and processes test file into a list of lists when called by launch()'''
    try:
        data = MissionData(filepath)    
    except IOError:
        print("Launch Test Data was not found at the specified location:", filepath)
        return sys.exit(1)
    data.planet = clean(data.lines[0], split=True)
    f = data.lines[1:]
    data.launch_cmds = [(clean(f[i], split=True),clean(f[i+1])) for i in range(0,len(f),2)]
    return data

def initialise_rovers(filepath):
    '''Function to start the mission! Initialises Rovers with instructions'''
    data = parse_test_data(filepath)
    planet = Planet(lat=int(data.planet[0]), lon=int(data.planet[1]))
    rovers = [Rover(landing=cmd[0], commands=cmd[1], planet=planet) for cmd in data.launch_cmds]
    return rovers

if len(sys.argv) > 1:
    rovers = initialise_rovers(sys.argv[1])
    for rover in rovers:
        rover.path()
        print(rover.report())
