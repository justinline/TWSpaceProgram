class Rover(object):
    '''Rover object that follows commands'''
    # On-board Navigation Mapping 'Bzzt
    compass = {'N':0,'E':1,'S':2,'W':3}
    turn = {'L':-1, 'R':1}
    rules =  [(0,1), (1,0), (0,-1), (-1,0)]
    
    def __init__(self, landing, commands, planet):
        self.x = int(landing[0])
        self.y = int(landing[1])
        self.heading = self.compass[landing[2]]
        self.commands = list(commands[0])
        self.planet = planet

    def path(self):
        #TODO: run through command list and call move()/rotate()
        pass
    
    def rotate(self, direction):
        direction = self.turn[direction]
        self.heading = (self.heading + direction) % 4

    def move(self):
        self.x += self.rules[self.heading][0]
        self.y += self.rules[self.heading][1]

    def report(self):
        for direction, value in self.compass.items():
            if value == self.heading:
                facing = direction
        print(self.x, self.y, facing)

