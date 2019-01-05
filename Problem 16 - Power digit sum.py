amical = [True]* 10001



total = 0

def diviseur(x):
    div = 0

    for i in range(1, x//2+1):
        if not(x%i):
            div += i

    return div


for i in range(2, 10001):
    if not amical[i]:
        continue

    somme = diviseur(i)
    if diviseur(somme) == i:
        total += i
        if somme < 10**4:
            total += somme
        amical[somme] = False
        amical[i] = False

print(total)
