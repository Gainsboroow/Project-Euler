from math import *

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

a = 1
for i in range(19,0,-1):
	a = lcm(int(a),i)
	print(a)
