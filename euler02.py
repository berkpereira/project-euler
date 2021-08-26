#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 12:22:58 2021

@author: gabrielpereira
"""

fibs = [1,2]

for n in range(2,100000):
    if fibs[n-1] + fibs[n-2] <= 4000000:
        fibs.append(fibs[n-1] + fibs[n-2])
    else:
        break
    
even_sum = 0

for term in fibs:
    if term % 2 == 0:
        even_sum += term

# Answer

print('See below list of relevant Fibonacci terms:')
for item in fibs:
    print(item)
    
print('And finally the actual sum of the even ones:')
print(even_sum)
