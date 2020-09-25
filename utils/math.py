from functools import reduce, lru_cache

def factors(n):
    """
    Returns the factors of the number n.

    Args:
        n (int): Number to be factored.

    Returns:
        set: Factors of number n.

    """
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_prime(n):
    """
    Check whether a number n is prime.

    Args:
        n (int): Non-negative integer.

    Returns:
        bool: True if n is prime else False.
    """
    return len(factors(n)) == 2

def prime_factors(n):
    """
    Return the prime factors of the number n.

    Args:
        n (int): Non-negative integer.

    Returns:
        set: Prime factors of number n.

    """
    return set(filter(is_prime, factors(n)))

@lru_cache(None)
def fib(n):
    """
    Return the n-th term of the Fibonacci sequence, starting with 1 as the
    first term. Return 0 if 0 is given.

    Args:
        n (int): Non-negative integer.

    Raises:
        ValueError: Non-integer or negative number is given.

    Returns:
        int: n-th term of the Fibonacci sequence.

    """
    if type(n) is not int:
        raise ValueError('Unable to handle input other than int.')
    if n < 0:
        raise ValueError('Unable to handle negative number as input.')

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)