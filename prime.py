"""Some methods related to prime number checking"""

from math import isqrt as math_isqrt
import functools
import typing

from error import NumValueError

__all__ = ["is_prime", 
           "not_prime", 
           "list_is_prime", 
           "list_not_prime",
           "PrimeRange"
] 


def is_prime(num: int) -> bool: 
    """Determine whether the number is a prime number"""
    if not isinstance(num, int):
        raise NumValueError("The num var must be an integer!")
    
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
    
def list_is_prime(num_list: list[int]) -> list[bool]:
    """Check if there are prime numbers in a list and return a list of boolean values."""
    if not num_list:
        return []
    result = []
    for num in num_list:
        if not isinstance(num, int):
            result.append(False)
        else:
            result.append(is_prime(num))
    return result

        
def list_not_prime(num_list: list[int]) -> list[bool]:
    """Check if there are ``not`` prime numbers in a list and return a list of boolean values."""
    return_list = list_is_prime(num_list)
    for i in range(len(return_list)):
        if isinstance(return_list[i], bool):
            return_list[i] = not return_list[i]
    return return_list
    

def PrimeRange(start: int, end: int) -> typing.Generator[int, None, None]:
    """Prime number range iterator: Generates prime numbers within [start, end] one by one."""
    current = max(start, 2)
    
    while current <= end:
        if current == 2:
            yield current
        elif current % 2 != 0: 
            is_p = True
            for i in range(3, int(current**0.5) + 1, 2):
                if current % i == 0:
                    is_p = False
                    break
            if is_p:
                yield current
        current += 1