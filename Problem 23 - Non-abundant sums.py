from math import sqrt 


"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper 
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed 
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def sommeDiviseur(n):
    total = 0
    for i in range(1, n//2 + 1):
        if not(n % i): total += i
    return total 

def recherche(cible):
    debut = 0
    fin = len(abondant) - 1

    somme = abondant[debut] + abondant[fin]
    while debut <= fin and somme != cible:
        if somme < cible:
            debut += 1
        if somme > cible:
            fin -= 1
        somme = abondant[debut] + abondant[fin]
    
    return somme == cible
    


abondant = []

print("RechercheAbondant")

for i in range(1, 28124):
    if sommeDiviseur(i) > i:
        abondant.append(i)

total = 0

print("RechercheNonSomme")

for i in range(1, 28124):
    if not(i % 1000): print(i)
    if not(recherche(i)):
        total += i

print(total)
