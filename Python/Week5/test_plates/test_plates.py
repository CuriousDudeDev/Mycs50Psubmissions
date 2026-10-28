from plates import is_valid

def test_less_than_minimum():
    assert is_valid('A') == False

def test_more_than_maximum():
    assert is_valid('AAAAAAA') == False

def test_middle_numbers():
    assert is_valid('ABC22A') == False

def test_no_punctuation():
    assert is_valid('AB 222') == False

def test_first_number():
    assert is_valid('ABC022') == False

def test_all_alpha():
    assert is_valid('HELLO') == True

def test_no_number_at_start():
    assert is_valid('00Hell') == False


