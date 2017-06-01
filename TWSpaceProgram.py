'''TW Space Program, launching Rovers onto mars!'''

import os # Required to read text files
import sys # Required to read command line args


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
    rovers = [Rover(data[i*2], data[(i*2)+1]) for i in range(int(len(data) / 2))]
    return rovers

class Rover(object):
    '''Rover object that follows commands'''
    compass = {'N':0,'E':1,'S':2,'W':3}
    rules =  [(0,1), (1,0), (0,-1), (-1,0)]
    def __init__(self, landing, commands):
        self.x = int(landing[0])
        self.y = int(landing[1])
        self.heading = self.compass[landing[2]]
        self.commands = list(commands[0]) # Breaks string into list of chars

    def path(self):
        for i in self.commands:
            print(i)
        pass
    
    def rotate(self, direction):

        pass
    
    def move(self):
        pass

    def report(self):
        print(self.x, self.y, self.heading)

    pass
