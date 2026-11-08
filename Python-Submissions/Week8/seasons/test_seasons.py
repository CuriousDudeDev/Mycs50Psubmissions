from seasons import final

def test_valid_date():
    assert final('2025-11-02') == 'Five hundred twenty-five thousand, six hundred minutes'
