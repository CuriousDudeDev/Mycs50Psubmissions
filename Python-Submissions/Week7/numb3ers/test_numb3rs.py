import pytest
from numb3rs import validate

def test_invalid_negative():
    assert validate('-1.-1.-1.-1') == False

def test_invalid_above_limit():
    assert validate('270.2309.3222.1233') == False

def test_invalid_words():
    assert validate('cat.dog') == False

def test_valid_ip():
    assert validate('1.2.3.4') == True

def test_range():
    assert validate('1.1.1.300') == False
