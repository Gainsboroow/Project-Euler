"""
Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr = 	n!/ ( r!(n−r)! ),where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater
than one-million?
"""

from math import *

tt = 0

def combi(n, p):
    return factorial(n)/(factorial(p)*factorial(n-p))


for n in range(1, 101):
    for p in range(1, n):
        if combi(n,p) >= 10**6:
            tt += 1

print(tt)
