import pytest
from TWSpaceProgram import upload_data,launch

@pytest.mark.skip
def test_upload_failure():
    assert upload_data(' ') == 1 

@pytest.mark.skip
def test_successful_upload():
    assert upload_data('tests/test.txt') == 0

def test_successful_launch():
    assert len(launch('tests/test.txt') ) > 0
    # Check that more than 1 rover was created

def test_unsuccessful_launch():
    assert launch('') == 1

class TestRovers(object):
    rovers = launch('tests/test.txt')
    def test_rover_1_landing(self):
        assert self.rovers[0].x == 1
        assert self.rovers[0].y == 2
        assert self.rovers[0].heading == 'N'
    
    def test_rover_numbers(self):
        assert len(self.rovers) == 2

    def test_rover_move(self):
        self.rovers[0].move()
        assert self.rovers[0].y == 3

    def test_change_heading(self):
        assert self.rovers[0].rotate('L') == 'W'
