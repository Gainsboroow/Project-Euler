"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K
text file containing nearly two-thousand common English words, how many are
triangle words?

Reponse :
162
"""

maxValue = 10 * 26 #max numbers of letter * max value of a letter

words = []
triangleNumber = [1/2*i*(i+1) for i in range(100)]

with open('Problem 42 - Coded triangle numbers.txt', 'r') as f:
    words = f.readline().replace('"', "").split(',')

total = 0

for i in words:
    score = 0
    for letter in i:
        score += ord(letter) - ord('A') + 1
    if score in triangleNumber:
        total += 1

print(total)
