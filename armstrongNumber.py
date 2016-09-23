def isArmstrongNumber(n):
	a = []
	t = n
	while t > 0:
		a.append(t%10)
		t /= 10
	k = len(a)
	'''
	s = 0
	for x in a:
		s += x ** k
	return s ==n
	'''
	return sum([x ** k for x in a]) == n

a = set()
for i in range(100,1000):
	if isArmstrongNumber(i):a.add(i)
print a