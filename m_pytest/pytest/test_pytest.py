import pytest
import math



def test_addition():
    assert 1 + 1 == 2

   
def test_sqrt():
    assert math.sqrt(10)**2 == pytest.approx(10, rel=1e-6)

def test_sqrt_negative():
    with pytest.raises(ValueError):
        math.sqrt(-1)
