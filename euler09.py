#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 00:11:55 2021

@author: gabrielpereira
"""

# PROBLEM: find product of unique pythagorean triple a,b,c such that a+b+c=1000

for a in range(1,1000):
    for b in range(1,1000):
        c = 1000 - a - b # Comes from rearranging one of the conditions for a,b,c
        if a**2 + b**2 == c**2:
            result = a*b*c
            triple = [a,b,c]
            break

print(f'Pythagorean triple: {triple}')
print(f"Triple's product: {result}")