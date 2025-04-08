'''
Created on 08.04.2025

@author: martinklonk
'''
import pytest
from martinSaysHello import sayHello

@pytest.fixture
def sayHelloInstance():
    return sayHello()

def testInstance():
    assert sayHelloInstance != None

def testSayJustHello():
    assert sayHelloInstance.greeting() == "Hallo!"