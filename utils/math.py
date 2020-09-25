from functools import reduce, lru_cache

class MathError(Exception):
    pass

def factors(n):
    """
    Returns the factors of number n.

    Args:
        n (int): Number to be factored.

    Returns:
        set: Factors of number n.

    """
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

@lru_cache(None)
def factorial(n):
    """
    Returns the factorial of non-negative integer n.

    Args:
        n (int): Non-negative integer.

    Raises:
        MathError: Non-integer or negative number is given.

    Returns:
        int: Factorial of n.

    """
    if type(n) is not int:
        raise MathError('Unable to handle input other than int.')
    if n < 0:
        raise MathError('Unable to handle negative number as input.')

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

@lru_cache(None)
def fibo(n):
    """
    Return the n-th term of the Fibonacci sequence, starting with 1 as the
    first term. Return 0 if 0 is given.

    Args:
        n (int): Non-negative integer.

    Raises:
        MathError: Non-integer or negative number is given.

    Returns:
        int: n-th term of the Fibonacci sequence.

    """

    if type(n) is not int:
        raise MathError('Unable to handle input other than int.')
    if n < 0:
        raise MathError('Unable to handle negative number as input.')

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)