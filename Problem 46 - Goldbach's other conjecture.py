"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""

def isPrime(n):
    for i in range(2, int(n**(1/2))+1):
        if not n % i: return False 
    return True 

premiers = [ i for i in range(2, 10**4) if isPrime(i)]
carres = [i**2 for i in range(10**4)]


for i in range(1, 10**4, 2):
    if isPrime(i): continue
    trouve = False
    for a in premiers:
        if a > i: break
        if (i-a)//2 in carres:
            trouve = True
            break
    
    if not trouve:
        print(i)
        break