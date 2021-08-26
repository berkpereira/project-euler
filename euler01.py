#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 12:12:44 2021

@author: gabrielpereira
"""

multiples35 = []

for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        multiples35.append(n)

print(sum(multiples35))