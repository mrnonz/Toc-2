from math import *
from random import *

def checkInradius(x, y):
	z = x**2 + y**2
	z = sqrt(z)

	if z < 1.0:
		return True
	else:
		return False

def monteCarlo(N):
	
	for i in range(N):
		random_x = random()
		random_y = random()

		print str(random_x) + ' ' + str(random_y)

	return 1.12

N = int(raw_input('Insert your N (random) :: '))

result = monteCarlo(N)

print 'N = ' + str(N) + ' :: Pi approx is --> ' + str(result*4)