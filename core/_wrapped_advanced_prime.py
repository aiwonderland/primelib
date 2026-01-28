import typing

from ._advanced_prime import (
    _euler_phi,
    _is_prime_miller_rabin,
    _prime_factorization,
    _sieve_of_eratosthenes
)

class SieveEratosthenes:
    """
    A single-responsibility class for Sieve of Eratosthenes algorithm.
    Generate all prime numbers less than or equal to a given maximum number.
    """

    def __init__(self, max_num: int):
        """
        Initialize the SieveEratosthenes instance with a maximum number.

        :param max_num: Upper bound for generating primes (integer ≥ 2 recommended).
        """
        if not isinstance(max_num, int):
            raise TypeError("max_num must be an integer.")
        self.max_num = max_num 
        self.primes = self._generate_primes()  

    def _generate_primes(self) -> typing.List[int]:
        """Instance method: Call private core sieve function to generate primes."""
        return _sieve_of_eratosthenes(self.max_num)

    @staticmethod
    def prime_factorization(num: int) -> typing.Dict[int, int]:
        """
        Static method: Prime factorization (optional, if you want to keep this function in the class).
        Decompose a positive integer into its prime factors and return their exponents.

        :param num: Integer to be factorized (≥ 2).
        :return: Dict with primes as keys and exponents as values.
        """
        if not isinstance(num, int):
            raise TypeError("num must be an integer.")
        return _prime_factorization(num)

    def __str__(self) -> str:
        # String representation of the instance.
        return f"SieveEratosthenes(max_num={self.max_num}, prime_count={len(self.primes)})"
    
    __repr__ = __str__

    def get_primes(self) -> typing.List[int]:
        """Public method: Get the generated list of primes."""
        return self.primes.copy() 
    

class EulerMillerRabinTools:
    """
    An independent utility class for two core prime-related operations:
    1. Euler's Totient Function (calculate coprime count)
    2. Miller-Rabin Primality Test (check big number for primality)
    """

    @staticmethod
    def euler_phi(num: int) -> int:
        """
        Public interface: Calculate Euler's Totient Function φ(n) (count of integers ≤ n that are coprime with n).
        
        Args:
            num: Positive integer (≥ 1) to calculate φ(n) for.
        
        Returns:
            int: Value of Euler's Totient Function φ(n).
        
        Raises:
            TypeError: If `num` is not an integer.
        """
        if not isinstance(num, int):
            raise TypeError("num must be an integer.")
        return _euler_phi(num)

    @staticmethod
    def is_prime_miller_rabin(num: int, test_rounds: int = 5) -> bool:
        """
        Public interface: Miller-Rabin Primality Test (probabilistic check for big number primality).
        
        Args:
            num: Integer to be tested for primality.
            test_rounds: Number of test rounds (more rounds = higher accuracy, default=5).
        
        Returns:
            bool: True if `num` is likely a prime, False if it's definitely a composite.
        
        Raises:
            TypeError: If `num` or `test_rounds` is not an integer, or `test_rounds` < 1.
        """
        if not isinstance(num, int):
            raise TypeError("num must be an integer.")
        if not isinstance(test_rounds, int) or test_rounds < 1:
            raise TypeError("test_rounds must be a positive integer.")
        return _is_prime_miller_rabin(num, test_rounds)

    def __str__(self) -> str:
        """String representation of the class instance."""
        return "EulerMillerRabinTools (Euler's Totient + Miller-Rabin Primality Test)"