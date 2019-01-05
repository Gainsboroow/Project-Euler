"""
It is possible to write five as a sum in exactly six
different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a
sum of at least two positive integers?

REPONSE :

"""


nombre = 100
dp = [-1]*(nombre+1)
dp[0] = dp[1] = dp[2] =  1

def facon(reste, methode):
    
    if dp[reste] != -1:
        return dp[reste]
    
    total = 0
    for i in range(1, reste//2 + 1 + reste % 2):
        temp = facon(reste - i, methode + "+" + str(i))
        total += temp
    
    dp[reste] = total
    return total

#print( facon(nombre, "") )

def facon2(somme, dernier, methode):
    #print(somme, dernier, methode)
    
    if somme > cible:
        return 0
    
    if somme == cible:
        #print(methode)
        return 1

    total = 0
    for i in range(1, dernier+1):
        total += facon2(somme + i, i, methode + ' ' + str(i) )

    return total


while 1:
    cible = int(input())
    print( facon2(0, cible, "") - 1)
