'''
Created on 08.04.2025

@author: martinklonk
'''
import pytest
from martinSaysHello import SayHello

@pytest.fixture
def sayHelloInstance():
    return SayHello()

def testInstance(sayHelloInstance):
    assert sayHelloInstance is not None

def testSayJustHello(sayHelloInstance):
    assert sayHelloInstance.greeting() == "Hallo!"
