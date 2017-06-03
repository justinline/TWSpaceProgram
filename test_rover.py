import pytest
from TWSpaceProgram import upload_data,launch

from shipyard import Rover
from space import Planet


TEST = 'tests/test.txt'

@pytest.mark.skip
def test_upload_failure():
    assert upload_data(' ') == 1 

@pytest.mark.skip
def test_successful_upload():
    assert upload_data(TEST) == 0

def test_successful_launch():
    assert len(launch(TEST) ) > 0
    # Check that more than 1 rover was created

def test_unsuccessful_launch(capsys):
    with pytest.raises(SystemExit):
        assert launch('') == 1

class TestSingleRover(object):
    planet = Planet(5,5)
    rover = Rover(['0', '0', 'N'], '', planet)
    def test_move(self):
        self.rover.move()
        assert self.rover.y == 1

    def test_change_heading(self):
        self.rover.rotate('L')
        assert self.rover.heading == 3

class TestRovers(object):
    rovers = launch(TEST)
    def test_rover_1_landing(self):
        assert self.rovers[0].x == 1
        assert self.rovers[0].y == 2
        assert self.rovers[0].heading == 0

    def test_rover_2_landing(self):
        assert self.rovers[1].x == 3
        assert self.rovers[1].y == 3
        assert self.rovers[1].heading == 1
    
    # Make Rovers follow their paths.
    for rover in rovers:
        rover.path() 
    
    def test_rover_1_report(self):
        assert self.rovers[0].report() == "1 3 N"    

    def test_rover_2_report(self):
        assert self.rovers[1].report() == "5 1 E"   

    def test_rover_numbers(self):
        assert len(self.rovers) == 2

    #TODO: Run through commands

    #TODO: Move and check end coordinates

class TestPlanet(object):
    planet = Planet(5,3)
    rover = Rover([0, 0, 'N'], ['MRMMLM'], planet)
    def test_1_planet(self):
        assert self.planet.area == (5, 3)
    def test_rover_on_planet(self):
        assert self.rover.planet == self.planet