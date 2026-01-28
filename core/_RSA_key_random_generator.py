import random
import math
from typing import Tuple, Dict

from ._RSA_core import (
    _generate_large_prime, _mod_inverse)
from ._advanced_prime import _is_prime_miller_rabin

class RSAGenerator:
    """
    Professional RSA Key Random Generator (compliant with RSA cryptography standards, supporting 1024/2048/4096-bit keys).
    Generated results include: Public Key (e, n), Private Key (d, n), and core intermediate parameters (p, q, φ(n)).
    """
    # Industry-standard public exponent (65537 - balances security and computational efficiency, avoids small exponent vulnerabilities)
    DEFAULT_PUBLIC_EXPONENT = 65537

    def __init__(self, bit_length: int = 1024):
        """
        Initialize the RSA generator with a specified key bit length.
        
        :param bit_length: Key bit length (≥ 512, recommended 1024/2048, must be an even integer).
        """
        self.bit_length = bit_length
        self.p, self.q = self._generate_distinct_primes() 
        self.n: int = 0
        self.phi_n: int = 0
        self.e: int = self.DEFAULT_PUBLIC_EXPONENT
        self.d: int = 0
  # Private key exponent

    def generate_keypair(self) -> Dict[str, Tuple[int, int]]:
        """
        Generate an RSA key pair (public key + private key).
        
        :return: Dictionary containing the key pair in the format {"public_key": (e, n), "private_key": (d, n)}.
        """
        # Step 1: Generate two distinct large prime numbers p and q
        self._generate_distinct_primes()
        
        # Step 2: Calculate the modulus n = p * q
        self.n = self.p * self.q
        
        # Step 3: Calculate Euler's totient function φ(n) = (p-1) * (q-1)
        self.phi_n = (self.p - 1) * (self.q - 1) # type: ignore
        
        # Step 4: Select and validate the public key exponent e (default 65537, ensure coprimality with φ(n))
        self._select_public_exponent()
        
        # Step 5: Calculate the private key exponent d (modular inverse of e with respect to φ(n))
        self.d = _mod_inverse(self.e, self.phi_n)
        
        # Step 6: Compile and return the key pair
        return {
            "public_key": (self.e, self.n),
            "private_key": (self.d, self.n)
        }

    def _generate_distinct_primes(self) -> Tuple[int, int]:
        """
        Generate two distinct large prime numbers p and q (internal helper method).
        :return: Tuple containing two distinct large primes (p, q)
        """
        p = _generate_large_prime(self.bit_length // 2)
        
        while True:
            q = _generate_large_prime(self.bit_length // 2)
            if q != p:
                break

        return (p, q)
    
    def _select_public_exponent(self) -> None:
        """Select the public key exponent e (ensure 1 < e < φ(n) and coprimality with φ(n)) (internal helper method)."""
        self.e = self.DEFAULT_PUBLIC_EXPONENT
        
        while math.gcd(self.e, self.phi_n) != 1:
            self.e = random.randint(2, self.phi_n - 1)

    def get_core_parameters(self) -> Dict[str, int]:
        """
        Retrieve the core intermediate RSA parameters (for debugging and maintenance purposes).
        
        :return: Dictionary containing p, q, n, φ(n), e, and d.
        :raises RuntimeError: If the key pair has not been generated yet.
        """
        if not self.n:
            raise RuntimeError("Please generate keypair first by calling generate_keypair()")
        
        return {
            "p": self.p,
            "q": self.q,
            "n": self.n,
            "phi_n": self.phi_n,
            "e": self.e,
            "d": self.d
        } 