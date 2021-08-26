#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 17:38:02 2021

@author: gabrielpereira
"""

# Want largest palindrome that's a product of two 3 digit numbers a and b

palindrome = [0]


# 2 nested loops for every combination of a and b
# Lots of repeated cases ((a,b) = (100,200) and (a,b) = (200,100) for example)

for a in range(999,100,-1):
    for b in range(999,100,-1):
        if str(a*b) == str(a*b)[::-1] and a*b > max(palindrome):
            palindrome.append(a*b)
            print(palindrome[-1])
        else:
            pass