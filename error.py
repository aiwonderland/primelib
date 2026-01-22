"""Errors in primelib."""

import time

__all__ = [
    "PrimelibException",
    "NumValueError"
]

class PrimelibException(Exception):
    """Common base class for all ``primelib`` exceptions."""
    pass

class NumValueError(PrimelibException):
    """raises when ``num`` value is not an integer."""
    pass