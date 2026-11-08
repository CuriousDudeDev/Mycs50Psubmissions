from twttr import shorten

def test_all_lower():
    assert shorten('hello') == 'hll'

def test_all_capital():
    assert shorten('HELLO') == 'HLL'

def test_no_vowels():
    assert shorten('SKY') == 'SKY'

def test_all_vowels():
    assert shorten('aaae') == ''

def test_numbers():
    assert shorten('123go') == '123g'

def test_punctuation():
    assert shorten('Me:Boy') == 'M:By'
