"""

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import *

def divisibilite(n):
    n = "X" + n
    if int(n[2:5]) % 2:
        return False
    if int(n[3:6]) % 3:
        return False
    if int(n[4:7]) % 5:
        return False
    if int(n[5:8]) % 7:
        return False
    if int(n[6:9]) % 11:
        return False
    if int(n[7:10]) % 13:
        return False
    if int(n[8:11]) % 17:
        return False
    return True

total = 0
chiffre = [str(i) for i in range(10) ]
for nombre in permutations(chiffre):
    if nombre[0] != "0" and divisibilite("".join(nombre)):
        total += int("".join(nombre))
        print(nombre)

print(total)



        
