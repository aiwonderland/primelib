"""A prime number - related library that offers a comprehensive set of functions for prime number operations."""

__version__ = "0.0.1"

from prime import (
    is_prime,
    not_prime,
    list_is_prime,
    list_not_prime
)
from error import (
    PrimelibException,
    NumValueError
)

__all__ = [
    "PrimelibException",
    "NumValueError",

    "is_prime", 
    "not_prime", 
    "list_is_prime", 
    "list_not_prime"
]