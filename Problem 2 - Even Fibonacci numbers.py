def fibo(n,a,b):
	suite = []
	c = 0
	for i in range(n):
	    c = a
	    a = a + b
	    b = c
	    if a < 4 * 1000 * 1000:
	        suite.append(a)
	return suite

x = [i for i in fibo(31,1,1) if i%2==0] #31 trouvé en tatonnant, 100 aurait donne le meme resultat
print(sum(x))
