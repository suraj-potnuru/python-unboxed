
import pytest
from src.app import add, divide

@pytest.mark.parametrize("a,b,expected_result", [
    (2,3,5),
    (1,1,2),
    (1,-1,0)
])
def test_add(a,b,expected_result):
    actual_result = add(a,b)
    assert expected_result == actual_result

def test_divide():
    expected_result = 2
    actual_result = divide(10, 5)
    assert expected_result == actual_result

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)