from random import randint
from typing import List, Dict


def _sieve_of_eratosthenes(max_num: int) -> List[int]:
    """Sieve of Eratosthenes: Generate all prime numbers less than or equal to max_num"""
    if max_num < 2:
        return []
    is_prime_arr = [True] * (max_num + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime_arr[i]:
            is_prime_arr[i*i : max_num+1 : i] = [False] * len(is_prime_arr[i*i : max_num+1 : i])
    
    primes = [num for num, is_p in enumerate(is_prime_arr) if is_p]
    return primes

def _prime_factorization(n: int) -> Dict[int, int]:
    """Prime Factorization: Decompose n into a product of prime numbers
      and return a dictionary in the format {prime number: exponent}"""
    factors = {}
    if n < 2:
        return factors
    
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n = n // 2
    
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n = n // i
        i += 2
    
    if n > 2:
        factors[n] = 1
    
    return factors

def _euler_phi(n: int) -> int:
    """Calculate Euler's totient function `φ(n)`: 
    the number of integers from 1 to n that are coprime with n"""
    if n == 1:
        return 1  
    if n < 1:
        return 0
    
    factors = _prime_factorization(n)
    result = n

    for p in factors.keys():
        result *= (p - 1)
        result //= p
    return result

def _is_prime_miller_rabin(n: int, k: int=10) -> bool:
    """Miller-Rabin Primality Test: Quickly determine whether a large number is a prime number
    :param n: Number to be judged
    :param k: Test times (more times = higher accuracy, default 10 for coin scene)
    :return: Whether it is a prime number
    """
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

