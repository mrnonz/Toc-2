from math import *

def checkInradius(x, y):
	z = x**2 + y**2
	z = sqrt(z)

	if z < 1.0:
		return True
	else:
		return False


N = int(raw_input('Insert your N (random) :: '))
