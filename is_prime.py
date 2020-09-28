# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:48:24 2020

@author: hana1602a
"""
if 0:
    def is_prime(n):
    
        """
        Assumes that n is a positive natural number
        """
        # We know 1 is not a prime number
        if n == 1:
            return False
    
        # We store the number of factors in this variable
        factors = 0
        # This will loop from 1 to n
        for i in range(1, n+1):
            # Check if `i` divides `n`, if yes then we increment the factors
            if n % i == 0:
                factors += 1
        # If total factors are exactly 2
        if factors == 2:
            return True
        return False
    
    # Test the above function
    for x in range(1, 11):
        print('%d: %s' % (x, is_prime(x)))
        
    
def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True

for x in range(1, 11):
    print('%d: %s' % (x, is_prime(x)))

# Output:
# 1: False
# 2: True
# 3: True
# 4: False
# 5: True
# 6: False
# 7: True
# 8: False
# 9: False
# 10: False

print('%d: %s' % (1000000000, is_prime(1000000000)))
# Output: 1000000000: False

print('%d: %s' % (1000000007, is_prime(1000000007)))    