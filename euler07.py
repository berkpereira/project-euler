#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:41:57 2021

@author: gabrielpereira
"""

import math

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


primes = [2]

n = 1

while len(primes) < 10001:
    if is_prime(n) == True:
        primes.append(n)
    
    n += 2 # Not checking even numbers
    
print(primes[10000])