#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 13:41:53 2021

@author: gabrielpereira
"""



print('Running check')

import math

# As factors are found, the list is updated with a new "large number" 
# resulting from the division of the previous one by the factor found
large_number = [600851475143]

# Create a list to keep note of the actual divisors of large_number[0]
successful_divisors = []

# Initialise the divisors to be tested
trial_divisor = 2


while trial_divisor <= math.floor(math.sqrt(large_number[-1])):

    if large_number[-1] % trial_divisor == 0:
        large_number.append(large_number[-1]/trial_divisor)
        successful_divisors.append(trial_divisor)
    else:
        trial_divisor += 1 # Only here is the trial updated so that square,... factors can be found
    
print(large_number) # Actually the largest factor is the last "large_number",
# as we can't find a factor for it (it's prime), and it's larger than the last successful_divisor
print(successful_divisors)