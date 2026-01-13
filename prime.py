"""Some methods related to prime number checking"""

from math import isqrt as math_isqrt
import functools
import typing

from error import NumNotIntError

__all__ = ["is_prime", "not_prime", "list_is_prime"] 

@functools.lru_cache(maxsize=None)
def is_prime(num: int) -> bool: 
    """Determine whether the number is a prime number"""
    if type(num) == float:
        raise NumNotIntError
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    _root = math_isqrt(num)
    for i in range(3, _root + 1, 2):
        if num % i == 0:
            return False
    return True  

def not_prime(num: int) -> bool:
    """Determine whether the number is not a prime number"""
    return_ = is_prime(num)
    if return_ == True:
        return False
    else:
        return True
    
def list_is_prime(num_list: typing.List[int]) -> list[bool]:
    """Check if there are prime numbers in a list and return a list of boolean values."""
    return_list = []
    for n in num_list:
        return_list.append(n)
    return return_list
        
# def list_not_prime(num_list: typing.List[int]) -> list[bool]:
#     """"""
    