# Test all function in prime.py
# useing `pytest`.

# import pytest

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prime import (
    is_prime,
    list_is_prime,
    not_prime,
    list_not_prime
)

def test_is_prime():  # 1 passed in 0.03s in 2026-1-16
    # Test the `is_prime` function
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(10) == False
    assert is_prime(97) == True
    assert is_prime(1000000007) == True

def test_list_is_prime():
    # Test the `list_is_prime` function
    assert list_is_prime([1, 2, 3, 4]) == [False, True, True, False]    
    assert list_is_prime([]) == []
    assert list_is_prime([5, 6, 7]) == [True, False, True]
    assert list_is_prime([0, -1, 2]) == [False, False, True]