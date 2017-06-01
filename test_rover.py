import pytest
from TWSpaceProgram import upload_data,launch

@pytest.mark.skip
def test_upload_failure():
    assert upload_data(' ') == 1 

@pytest.mark.skip
def test_successful_upload():
    assert upload_data('tests/test.txt') == 0

def test_successful_launch():
    assert launch('tests/test.txt') != []

def test_unsuccessful_launch():
    assert launch('') == 1