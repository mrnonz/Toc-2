from math import *
from decimal import *

precision = 10**(-50)
precContext = 1000

myothercontext = Context(precContext, rounding=ROUND_HALF_DOWN)
setcontext(myothercontext)


def average(x, y):
	return Decimal((x + y)) / Decimal(2.0)


def improve(guess, number):
	return average(guess, number/guess)


def good_enough(guess, number):
	temp = guess**2
	temp -= number
	return abs(temp) < precision


def sqrt_apox(guess, number):
	while not good_enough(guess, number):
		guess = improve(guess, number)

	return guess


def sqrtNewton(number):
	return sqrt_apox(1, number)


findSqrt = int(raw_input("Insert your number [sqrt] :: "))

print "Sqrt(%s) = %s" % (findSqrt, sqrtNewton(findSqrt))
