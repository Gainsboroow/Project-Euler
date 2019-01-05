"""
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

decimales = "0"
nombre = 1

while len(decimales) <= 10**6 + 1:
    decimales += str(nombre)
    nombre += 1

d1 = int(decimales[1])
d10 = int(decimales[10])
d100 = int(decimales[100])
d1000 = int(decimales[1000])
d10000 = int(decimales[10000])
d100000 = int(decimales[100000])
d1000000 = int(decimales[1000000])

total = d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

print(total)