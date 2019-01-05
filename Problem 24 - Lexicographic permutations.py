from itertools import *

a = list( permutations(range(10), 10) )
print( a[10**6-1] )
