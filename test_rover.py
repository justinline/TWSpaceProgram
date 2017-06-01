import pytest
from TWSpaceProgram import upload_data


def test_upload_failure():
    assert upload_data(' ') == 1 

def test_successful_upload():
    assert upload_data('tests.txt') == 0
