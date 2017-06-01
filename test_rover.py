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

def test_rover_1_landing():
    rovers = launch('tests/test.txt')
    assert rovers[0].landing == ['1', '2', 'N']