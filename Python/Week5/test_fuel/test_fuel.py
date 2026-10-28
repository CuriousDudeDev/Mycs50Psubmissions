from fuel import convert , gauge

def test_convert_proper_fraction():
    assert convert('3/4') == 75

def test_convert_0_fraction():
    assert convert('4/0') == 'Division by zero is not supported'
