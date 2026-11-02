from jar import Jar
import pytest

def test_init():
    jar = Jar(13)
    assert jar.capacity == 13


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2


def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

def test_invalid_1():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
def test_invalid_2():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(2)

