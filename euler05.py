#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 17:57:28 2021

@author: gabrielpereira
"""

# Simple function to calculate factorial of given int

def factorial(number):
    if number == 0:
        return 1
    else:
        output = 1
        for n in range(1,number+1):
            output = output * n
        return output

# Function to determine whether given number is divisible by all ints up to divisor

def divisible_up_to(number,divisor):
    for n in range(1,divisor+1):
        if number % n != 0:
            return False
    else:
        return True



# PROBLEM: Want smallest int evenly disible by all ints from 1 to 20

# Start with a known one, factorial(20):

divisible_number = factorial(20)


# Now divide factorial(20) by progressively larger numbers until the
# resulting number is no longer divisible by all ints up to 20

n = 2

while n <= 20:
    if divisible_up_to(divisible_number/n,20) == True:
        divisible_number = divisible_number//n
    else:
        n += 1
        
print(divisible_number)