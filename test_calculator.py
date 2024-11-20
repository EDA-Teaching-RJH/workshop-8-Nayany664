import pytest
from calculator import main
from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

def main():
    test1() # you need to use the word test cause it's 'pytest'
    test2()
    test3()
    test4()

def test1() :
    try:
        assert add(1,2) == 3
    except (AssertionError, NameError):
        print("1 + 2 is not 3")
def test2() :
    try:
        assert subtract(1,2) == -1
    except (AssertionError, NameError):
        print("1 - 2 is not -1")
def test3() :
    try:
        assert multiply(1,2) == 2
    except (AssertionError, NameError):
        print("1 * 2 is not 2")
def test4() :
    try:
        assert divide(1,2) == 0.5
    except (AssertionError, NameError):
        print("1 / 2 is not 0.5")
    except (ZeroDivisionError, NameError):
        print("Cannot divide with 0")

if __name__ == "__main__" : #determines whether currect script is being run as main program or if it's being imported as a module into another script
    main()

    #when running type in 'pytest test_calculator.py'