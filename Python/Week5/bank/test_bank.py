from bank import value

def test_hello_name():
    assert value('hello, meow-cat') == '$0'

def test_only_hello():
    assert value('hello') == '$0'

def test_starts_with_h_and_not_hello():
    assert value('hey') == '$20'

def test_starts_with_h_plus_name():
    assert value('hey , neymar') == '$20'

def test_other_greeting():
    assert value('whatsup') == '$100'

def test_other_greeting_with_name():
    assert value('wassup, ronaldo') == '$100'

def test_space_hello():
    assert value(' hello') == '$0'

def test_space_otherh():
    assert value(' hey') == '$20'

def test_upper_hello():
    assert value('HELLO! DUDE') == '$0'

def test_upper_other_h():
    assert value('HEY! MAN') == '$20'

def test_upper_other_greeting():
    assert value('WAASSUUP MAN') == '$100'
