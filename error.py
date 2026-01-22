"""Errors in primelib."""

import time

__all__ = [
    "PrimelibException",
    "NumValueError"
]

class PrimelibException(Exception):
    """Common base class for all ``primelib`` exceptions."""
    def __init__(self, message=""):
        super().__init__(message)

class NumValueError(PrimelibException):
    """raises when ``num`` value is not an integer."""
    pass