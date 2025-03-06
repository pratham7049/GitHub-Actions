# app.py
# This is a test commit

def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b  

def test_add():
    """Tests the add function with multiple cases."""
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10
    assert add(100, 200) == 300

