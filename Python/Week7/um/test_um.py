from um import count

def test_upper():
    assert count('UM I LIKE BOOKS') == 1

def test_lower():
    assert count('um i like books') == 1

def test_snake_case():
    assert count('um_i_like_books') == 0

def test_camel_case():
    assert count('Um ILikeBooks') == 1

def test_um_in_other_word_in_middle():
    assert count('I um like meowmewowumcatcat') == 1

def test_um_in_other_word_start():
    assert count('I um like an umbrella') == 1

def test_um_in_other_word_end():
    assert count('I um like album') == 1
