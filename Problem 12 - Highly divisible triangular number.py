from math import *

def nbDiviseurs(nombre):
    total = 1
    
    for i in range(1, nombre//2 + 1 ):
        if not(nombre % i):
            total += 1


    return total

nombre = 0

for i in range(1, 1000000):
    if not( i % 1000):
        print(i)
    nombre += i

    if nbDiviseurs(nombre) > 500:
        print(nombre)
        break
