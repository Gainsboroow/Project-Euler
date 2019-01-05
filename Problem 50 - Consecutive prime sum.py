"""


The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to
a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from math import sqrt

f = open("premier.txt", "r")


tt = 0
consecutiveSum = [0]

for i in f:
    if consecutiveSum[-1] + int(i) >= 10**6:
        break
    consecutiveSum.append( consecutiveSum[-1] + int(i) )
f.close()

def isPrime(n):    
    for i in range(2, int(sqrt(n))+1):
        if not n % i : return False
    return True

for debut in range(len(consecutiveSum)):
    for fin in range(debut, len(consecutiveSum)):
        somme = consecutiveSum[fin] - consecutiveSum[debut]
        if isPrime(somme):
            #print(somme)
            tt = max(tt, somme)

print(tt)
