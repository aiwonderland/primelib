"""Errors in primelib"""
class NumNotIntError(Exception):
    """raises when ``num`` is ``float``."""

    def __init__(self):
        super().__init__("The nim value must be a integer!")