from math import *

def checkInradius(x, y):
	z = x**2 + y**2
	z = sqrt(z)

	if z < 1.0:
		return True
	else:
		return False

def monteCarlo(N):
	return 1.23

N = int(raw_input('Insert your N (random) :: '))

result = monteCarlo(N)

print 'N = ' + str(N) + ' :: Pi approx is --> ' + str(result)