"""
Python solution to the `Cross base primes problem`
"""

from math import sqrt


def convert(n, base):
    """
    Function to convert number n to any base
    """
    base_chars = "0123456789ABCDEF"
    if n < base:
        return base_chars[n]
    return convert(n // base, base) + base_chars[n % base]

def is_prime(n):
    """
    Function to check primality
    """
    if n <= 1:
        return False
    elif n in [2, 3]:
        return True 
    elif n % 6 not in [1, 5]:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2): # change range to xrange for python2
        if n % i == 0:
            return False
    return True

def is_cross_base_prime(n, base):
    """
    Function to check whether a number is a cross-base-prime or not
    """
    if is_prime(n) and is_prime(int(convert(n, base))):
        return True
    return False


def main():
    print(is_cross_base_prime(69, 2))       # False
    print(is_cross_base_prime(131, 16))     # True
    print(is_cross_base_prime(1312, 8))     # False
    print(is_cross_base_prime(67, 11))      # True

if __name__ == "__main__":
    main()
