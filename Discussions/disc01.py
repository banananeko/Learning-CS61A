def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining

def is_prime(n): 
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    divider = 2
    result = True
    while divider <= n // 2:     # the largest divider is half of the number
        if n % divider == 0:
            result = False
        divider += 1
    return result