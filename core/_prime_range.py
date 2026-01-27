import typing

from error import PrimeRangeError, PrimeInfiniteRangeError

__all__ = [
    "PrimeRange",
    "PrimeInfiniteRange"
]

def PrimeRange(start: int, end: int) -> typing.Generator[int, None, None]:
    """
    Generate prime numbers within a specified integer range [start, end] as a generator.
    
    This function yields prime numbers one by one, optimizing by skipping even numbers 
    (except 2, the only even prime) and checking divisibility only up to the square root 
    of the current number for efficiency.
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise PrimeRangeError("start and end must be integers")
    if start > end:
        raise PrimeRangeError("start cannot be greater than end")
    current = max(start, 2)
    
    while current <= end:
        if current == 2:
            yield current
        elif current % 2 != 0: 
            is_p = True

            for i in range(3, int(current**0.5) + 1, 2):
                if current % i == 0:
                    is_p = False
                    break

            if is_p:
                yield current
        current += 1


def PrimeInfiniteRange(start: int = 2) -> typing.Generator[int, None, None]:
    """
    Generate an infinite sequence of prime numbers starting from a specified integer as a generator.
    
    This function yields primes indefinitely (never terminates), with the same optimization 
    as PrimeRange (skipping even numbers, checking up to square root). Useful for scenarios 
    where an unbounded stream of primes is needed.
    """
    if not isinstance(start, int):
        raise PrimeInfiniteRangeError("start must be an integer")
    current = max(start, 2)

    while True:
        if current == 2:
            yield current
        elif current % 2 != 0:
            is_p = True

            for i in range(3, int(current**0.5) + 1, 2):
                if current % i == 0:
                    is_p = False
                    break

            if is_p:
                yield current
        current += 1