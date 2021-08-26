#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 00:55:58 2021

@author: gabrielpereira
"""

import math

# Basic primality test function
# Function originally created for euler7.py
def is_prime(integer: int) -> bool:
    if integer == 1:
        return False
    elif integer == 2:
        return True
    elif integer % 2 == 0:
        return False
    else:
        for n in range(3 , math.floor(integer**0.5) + 1 , 2):
            if integer % n == 0:
                return False
        else:
            return True
        

prime_sum = 2 # Odd numbers will be skipped in the loop, so 2 will be included right away

for number in range(1,2000000,2):
    if is_prime(number) == True:
        prime_sum = prime_sum + number
    else:
        pass
    
print(f'Sum of primes up to 2 million: {prime_sum}')

# COULD'VE USED SIEVE OF ERATOSTHENES TO FIND ALL THOSE PRIMES INSTEAD