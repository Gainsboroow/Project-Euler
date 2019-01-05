"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.

REPONSE : 
145 et 40585
Total :  40730
"""

from math import factorial 

total = 0

for i in range(3, 10**5):
    temp = sum([factorial(int(chiffre)) for chiffre in str(i)])
    if temp == i:
        print(i)
        total += i

print("Total : ", total)
