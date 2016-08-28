from __future__ import division
from math import *
from random import *
from decimal import *

def checkInradius(x, y):
	z = x**2 + y**2
	z = sqrt(z)

	if z < 1.0:
		return True
	else:
		return False

def monteCarlo(N):

	countInradius = 0
	
	for i in range(N):
		random_x = random()
		random_y = random()

		if checkInradius(random_x, random_y):
			countInradius += 1

	result = countInradius / N

	return Decimal(result)

N = int(raw_input('Insert your N (random) :: '))

result = monteCarlo(N)

print 'N = ' + str(N) + ' :: Pi approx is --> ' + str(result*4)