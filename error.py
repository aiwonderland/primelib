"""Errors in primelib."""


__all__ = [
    "PrimelibException",
    "NumValueError",
    "PrimeRangeError",
    "PrimeInfiniteRangeError"


]

class PrimelibException(Exception):
    """Common base class for all ``primelib`` exceptions."""
    def __init__(self, message=""):
        super().__init__(message)

class NumValueError(PrimelibException):
    """raises when ``num`` value is not an integer."""
    pass
    
class PrimeRangeError(PrimelibException):
    """Raises when `start`/`end` is not integer or `start` > `end`."""
    pass

class PrimeInfiniteRangeError(PrimelibException):
    """Raises when `start` value is not an integer."""
    pass
