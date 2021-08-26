#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:22:24 2021

@author: gabrielpereira
"""

# PROBLEM: Calculate (1 + 2 + ... + 100)^2 - (1^2 + 2^2 + ... + 100^2)

square_of_sums = (sum(list(range(1,101))))**2

sum_of_squares = 0
for n in range(1,101):
    sum_of_squares = sum_of_squares + n**2

print(square_of_sums - sum_of_squares)