#Méthode 1
a = sum([x**2 for x in range(101)])
b = (100*101/2)**2
c = b - a
print(c)

#2e méthode
a = 0
b = 0
c = 0
for i in range(101):
    a += i**2
    b += i

b = b * b
c = b - a
print(c)
