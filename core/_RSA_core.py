"RSA core."

from random import getrandbits
from typing import Tuple

from ._advanced_prime import _is_prime_miller_rabin

def _generate_large_prime(bit_length: int = 1024) -> int:
    """
    Generate a large prime number with the specified bit length (RSA recommends at least 1024 bits, and 2048 bits is more secure).

    :param bit_length: The bit length of the prime number (must be an even number and ≥ 512).
    :return: A large prime number that meets the required bit length.
    """
    if not isinstance(bit_length, int) or bit_length < 512 or bit_length % 2 != 0:
        raise ValueError("bit_length must be an even integer ≥ 512 (recommended 1024/2048)")
    
    while True:
        candidate = getrandbits(bit_length)
        candidate |= (1 << (bit_length - 1)) | 1
        if _is_prime_miller_rabin(candidate):
            return candidate
        
def _mod_inverse(a: int, m: int) -> int:
    """
    xtended Euclidean Algorithm to calculate the modular inverse (solve for x in the congruence ax ≡ 1 (mod m)).

    :param a: The integer for which to find the modular inverse.
    :param m: The modulus.
    :return: The modular inverse of a with respect to m.
    :raises ValueError: Raised when a and m are not coprime, as no modular inverse exists in this case.
    """
    def _extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = _extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x
    
    gcd, x, _ = _extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"No modular inverse exists for {a} mod {m} (they are not coprime)")
    else:
        return x % m