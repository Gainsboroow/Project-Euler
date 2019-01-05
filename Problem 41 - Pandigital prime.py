"""
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?

REPONSE :
7652413"""

premier = []
with open("premier.txt", "r") as f:
    for i in f:
        premier.append(int(i))


def isPandigital(n):
    used = [0 for i in range(10)]
    for i in n:
        used[int(i)] += 1
    for i in used[1:len(n)+1]:
        if i != 1:
            return False
    return True

def isPrime(n):
    for i in premier:
        if i >= n : return True
        if not n % i : return False
    return True

maxi = 0

puiss = 7
i = 10**puiss - 1
while i > 10**(puiss-1):
    if not i % 10**6: print(i / 10**6, "%")
    
    if "0" in str(i):
        for indice, a in enumerate(str(i)):
            if a == "0":
                break
            
        i = int( str(i)[:indice] + "0"*(len(str(i)) - indice) ) - 1
        
    if isPandigital(str(i)) and isPrime(i):
        maxi = i
        break

    i -= 2
    
print(maxi)
            
