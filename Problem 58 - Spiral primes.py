"""
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

REPONSE :
26241.0
0.09999809454850327

"""

from math import sqrt

def isPrime(n):
    if n < 3: return False #2 Excluded, not on the diagonal
    for i in range(2, int(sqrt(n))+1):
        if not(n % i) : return 0
    return 1


cote = 100000

etape = 1

indice = 0

nbPrime = 0

i = 1
try:
    while i < cote**2:
        for a in range(etape):
            if not(i % 10**6): print(i)
            i += 1
            
        indice = (indice+1) % 4
        if not(indice % 2):
            etape += 1

        nbPrime += isPrime(i)
        
        if sqrt(i-1) == int(sqrt(i-1)):
            ratio = nbPrime / (2*sqrt(i-1)-1)
            if i != 2 and ratio < 0.1:
                print(i, sqrt(i-1))
                break
except:
    pass
print(ratio)
