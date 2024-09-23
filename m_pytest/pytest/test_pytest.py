import pytest
import math



def test_addition():
    assert 1 + 1 == 2

@pytest.mark.xfail
def test_sqrt():
    assert math.sqrt(10)**2 == 10   

def test_sqrt_negative():
    with pytest.raises(ValueError):
        math.sqrt(-1)

def test_failure1():
    print("lots\nof\nstuff")
    assert False

def test_failure2(self):
    print("still\nmore\nstuff")
    assert False