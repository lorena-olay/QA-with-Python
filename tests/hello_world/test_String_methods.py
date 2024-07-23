def test_upper():
    assert "hello world".upper() == 'HELLO WORLD'

def test_isupper():
    assert not "hello world".isupper()
    assert "HELLO".isupper()

# archivo test_string_methods.py
def test_upper():
    assert "hello world".upper() == 'HELLO WORLD'

def test_isupper():
    assert not "hello world".isupper()
    assert "HELLO".isupper()

# pytest test_string_methods.py