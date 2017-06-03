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
        self.commands = commands
        self.planet = planet

    def execute_commands(self):
        for command in self.commands:
            if command == 'M':
                self.move()
            else:
                self.rotate(command)
    
    def rotate(self, direction):
        direction = self.turn[direction]
        self.heading = (self.heading + direction) % 4

    def move(self):
        self.x += self.rules[self.heading][0]
        self.y += self.rules[self.heading][1]
        #TODO: Check Boundaries - Needs rule

    def report(self):
        for direction, value in self.compass.items():
            if value == self.heading:
                facing = direction
        return str(self.x) + " " + str(self.y) + " " + str(facing)

