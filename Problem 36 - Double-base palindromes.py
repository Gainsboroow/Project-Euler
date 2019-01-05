"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

REPONSE :
872187
"""

def estPalindrome(n):
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True

total = 0

for i in range(10**6):
    if estPalindrome(str(i)) and estPalindrome(bin(i)[2:]):
        total += i
        
print(total)
