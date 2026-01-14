"""Errors in primelib."""

import time

__all__ = [
    "PrimelibException",
    "NumValueError"
]

class PrimelibException(Exception):
    """Common base class for all ``primelib`` exceptions."""

    def __init__(self, error_codes: str, error_msg: str | None, error_code: int | None) -> None:
        self.error_codes = error_codes
        self.error_msg = error_msg
        self.error_code = error_code
        self.error_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.main_msg = f"{self.error_codes} - {self.error_msg}"
        super().__init__(self.main_msg)

    def get_error_codes(self):
        """Return the ``error_codes`` in Error"""
        return self.error_codes
    
    def get_error_msg(self):
        """Return the ``error_msg`` in Error"""
        return self.error_msg
        
    def format_message(self, format_msg: str | None):
        """Standardize the format of error messages
        
        :param format_msg: Define the classification of error messages.
            It can be: ``Standard`` ``Format`` ``ClearlyIndicated``"""
        if format_msg == "Standard":
            self.main_msg = f"error type: {self.error_codes}, error message: {self.error_msg}"
        if format_msg == "Format":
            self.main_msg = f"{self.error_codes} ({self.error_code}): {self.error_msg}"
        if format_msg == "ClearlyIndicated":
            self.main_msg = f"{self.error_time} happen error {self.error_codes}: {self.error_msg} error_code: {self.error_code}"

class NumValueError(PrimelibException):
    """raises when ``num`` value is not an integer."""
    pass