"""A prime number - related library that offers a comprehensive set of functions for prime number operations.

This module also includes numerous advanced prime number operations, including the RSA encryption algorithm.

This project is licensed under the MIT License - see the LICENSE file for details."""

__version__ = "0.0.1"

from prime import *
from core._prime_range import *
from core._wrapped_advanced_prime import (
    SieveEratosthenes,
    EulerMillerRabinTools)
from core._RSA_key_random_generator import RSAGenerator
import error

__all__ = [
    "error",

    "is_prime", 
    "not_prime", 
    "list_is_prime", 
    "list_not_prime",

    "PrimeRange",
    "PrimeInfiniteRange",

    "SieveEratosthenes",
    "EulerMillerRabinTools",

    "RSAGenerator"
]