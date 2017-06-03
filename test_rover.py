import pytest
from tw_space_program import parse_test_data, initialise_rovers

from shipyard import Rover
from space import Planet


TEST = 'tests/test.txt'


@pytest.mark.skip
def test_upload_failure():
    assert parse_test_data(' ') == 1


@pytest.mark.skip
def test_successful_upload():
    assert parse_test_data(TEST) == 0


def test_successful_launch():
    assert len(initialise_rovers(TEST)) > 0
    # Check that more than 1 rover was created


def test_unsuccessful_initialise_rovers(capsys):
    with pytest.raises(SystemExit):
        assert initialise_rovers('') == 1


class TestSingleRover(object):
    planet = Planet(5, 5)
    rover = Rover(['0', '0', 'N'], '', planet)

    def test_move(self):
        self.rover.move()
        assert self.rover.y == 1

    def test_change_heading(self):
        self.rover.rotate('L')
        assert self.rover.heading == 3


class TestRovers(object):
    rovers = initialise_rovers(TEST)

    def test_rover_1_landing(self):
        assert self.rovers[0].x == 1
        assert self.rovers[0].y == 2
        assert self.rovers[0].heading == 0

    def test_rover_2_landing(self):
        assert self.rovers[1].x == 3
        assert self.rovers[1].y == 3
        assert self.rovers[1].heading == 1

    def test_rover_1_report(self):
        self.rovers[0].execute_commands()
        assert self.rovers[0].report() == "1 3 N"

    def test_rover_2_report(self):
        self.rovers[1].execute_commands()
        assert self.rovers[1].report() == "5 1 E"

    def test_rover_3_double_digit_report(self):
        self.rovers[2].execute_commands()
        assert self.rovers[2].report() == "0 11 E"

    def test_rover_numbers(self):
        assert len(self.rovers) == 3


class TestPlanet(object):
    planet = Planet(5, 3)
    rover = Rover([0, 0, 'N'], ['MRMMLM'], planet)

    def test_1_planet(self):
        assert self.planet.area == (5, 3)

    def test_rover_on_planet(self):
        assert self.rover.planet == self.planet
