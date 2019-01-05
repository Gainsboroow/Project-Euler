def suite(a):
    return a//2 if a % 2 == 0 else 3*a+1

def nbEtapes(nombre):
    if nombre == 1:
        return 0
    if nombre < 10**8:
        if cache[nombre] != 0:
            return cache[nombre]

    etapes = nbEtapes( suite(nombre) ) + 1
    if nombre < 10**8:
        cache[nombre] = etapes
    return etapes


cache = [0] * 10**8
longueurMax = -1
nombre = -1

for i in range(2, 10**6):
    etape = nbEtapes(i)
    if etape > longueurMax:
        longueurMax = etape
        nombre = i

print(nombre)
