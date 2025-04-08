import pytest
from thing import Thing
import sys
print(sys.path)

@pytest.fixture
def thing():
    return Thing("Bob")


def test_correct_greeting(thing):
    assert "Hello Bob!" == thing.return_hello_name()


def test_fail(thing):
    assert "Wrong!" == thing.return_hello_name()
