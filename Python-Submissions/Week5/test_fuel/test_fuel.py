from fuel import convert , gauge
import pytest

def test_convert_proper_fraction():
    assert convert('3/4') == 75

def test_convert_raises_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('2/0')

def test_convert_numerator_big_than_denominator():
    with pytest.raises(ValueError):
        convert('4/2')

def test_convert_not_numbers():
    with pytest.raises(ValueError):
        convert('dude/bro')

def test_convert_negative_fractions():
    with pytest.raises(ValueError):
        convert('-1/3')

def test_percent_full():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

def test_percent_none():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'

def test_percent_normal():
    assert gauge(75) == '75%'

