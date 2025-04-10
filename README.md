# Project layout

- `app` contains dummy package to be tested 
- `tests` contains tests definitions 

# Python with pytest


## Installation
Simply install pytest & pytest-mock :
```
pip install -U pytest
pip install -U pytest-mock
```
or if using python >= 3 on a Mac :
```
pip3 install -U pytest
pip3 install -U pytest-mock
```

or alternatively:
Create virtual environment...
```bash
python3 -m venv VENV
```
...activate it:
```bash
source VENV/bin/activate
```
...and install requirements listed in requirements.txt file:
```
pip install -r requirements.txt
```

## Run
 - Write your test in a python file (```test_thing.py``` in the example)
 - run : ```python -m pytest tests/test_thing.py```
 - run tests with coverage: ```python3 -m pytest --cov=app tests/```
 - or if using python >= 3 on a Mac : ```python3 -m pytest tests/test_thing.py```
 - or if using VSCode + Python extension, right-click any test and select 'Run All Tests' (select 'pytest' when prompted to configure a test framework)
 - or if using PyCharm:
   - First you would need to [set up test runner](https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#choose-test-runner) for project:
     - Open Project preferences (On Mac - ⌘,)
     - Navigate into `Tools -> Python integrated tools -> Testing -> Test runner`
     - Choose `pytest`
   - After that you can click on `tests` folder or individual test and either choose to
     - Run default runner using shortcut (On Mac - ⇧^R)
     - Manually choose test configuration under `More Run/Debug` menu - for example, in order to run tests with coverage

## Other
An alternate version with before fixture is provided in the ```test_thing_fixture.py``` file.

To run same as before :
```python -m pytest tests/test_thing_fixture.py``` or ```python3 -m pytest tests/test_thing_fixture.py```

## Resources

 - <http://pythontesting.net/framework/pytest/pytest-introduction/>
 - <https://docs.pytest.org/en/latest/getting-started.html>

## run from docker

 ```
 './docker_test.sh'
 ```
 
 ---
 
# Bowling Kata
 ein Übungsprojekt für die ILV Software Testing an der FH Campus Wien
 
## Bowlingregeln
- Das Spiel besteht aus 10 Frames. In jedem Frame hat der Spieler zwei Würfe, um 10 Pins umzuwerfen. Die Punktzahl für den Frame ergibt sich aus der Gesamtzahl der umgeworfenen Pins, plus Boni für Strikes und Spares.
- Ein Spare ist, wenn der Spieler alle 10 Pins in zwei Würfen umwirft. Der Bonus für diesen Frame ist die Anzahl der Pins, die beim nächsten Wurf umgeworfen werden.
- Ein Strike liegt vor, wenn der Spieler alle 10 Pins mit seinem ersten Wurf umwirft. Der Frame wird dann mit einem einzigen Wurf abgeschlossen. Der Bonus für diesen Frame ist der Wert der nächsten beiden Würfe.
- Im zehnten Frame darf ein Spieler, der einen Spare oder Strike geworfen hat, die zusätzlichen Kugeln werfen, um den Frame abzuschließen. Es können jedoch nicht mehr als drei Kugeln im zehnten Frame geworfen werden.

---

## Aufgabe:
Schreibe Sie eine Klasse `Game`, die zwei Methoden hat
- `void roll(int)` wird jedes Mal aufgerufen, wenn der Spieler eine Kugel wirft. Das Argument ist die Anzahl der umgeworfenen Pins. 
- `int score()` gibt die Gesamtpunktzahl für dieses Spiel zurück.

