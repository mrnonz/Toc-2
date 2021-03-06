from __future__ import division
from math import *
from random import *
from decimal import *
import time


def checkInradius(x, y):
	z = x**2 + y**2
	z = sqrt(z)

	if z < 1.0:
		return True
	else:
		return False


def monteCarlo(N):

	countInradius = 0
	stopPrint = 1

	method_starts = time.time()
	for i in range(N):
		random_x = random()
		random_y = random()

		if checkInradius(random_x, random_y):
			countInradius += 1

		if i+1 == stopPrint:

			result = Decimal(countInradius / (i+1))
			result *= 4

			now = time.time()
			rount_time = float("{0:.5f}".format(now - method_starts))
			print "[Time " + str(rount_time) + " s] When sample space is " + str(stopPrint) + ' :: Pi is ' + str(result)

			stopPrint *= 10


N = int(raw_input('Insert your Maximum sample space :: '))

monteCarlo(N)
