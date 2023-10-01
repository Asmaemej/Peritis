import pytest
from exo2 import find_path


def test_find_path():
    # Test case 1: Start from node '7'
    assert find_path('7') == ['7', '3', '15', '16', '1', '8', '0', '4', '17', '18']

    

if __name__ == '__main__':
    pytest.main()
