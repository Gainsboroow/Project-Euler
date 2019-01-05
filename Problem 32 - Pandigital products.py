from math import *

"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Reponse:
45228
"""

total = 0

dejaVu = [False]*(10**8)

print("Start")

for a in range(10**3):
    if not a % 10**3: print(a)
    for b in range(a+1, 10**4):
        used = [False] * 10

        produit = a*b

        if dejaVu[produit]: break

        tailleA = len(str(a))
        tailleB = len(str(b))
        tailleProd = len(str(produit))

        if tailleA + tailleB + tailleProd != 9:
            continue 
        
        arreter = False 
        for i in str(a):
            if used[int(i)] : 
                arreter = True
                break
            used[int(i)] = True 
        
        if arreter : continue 

        for i in str(b):
            if used[int(i)] : 
                arreter = True
                break
            used[int(i)] = True 

        if arreter : continue 
        
        for i in str(produit):
            if used[int(i)] : 
                arreter = True
                break
            used[int(i)] = True 

        for i in range(1,10):
            if not(used[i]):
                arreter = True
                break

        if not arreter:
            total += produit 
            dejaVu[produit] = 1
            
print(total)
