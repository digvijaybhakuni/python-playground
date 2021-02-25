
# Get the square root of number

import math
#from math import sqrt
#from math import *

def rootfunc(num):
	print math.sqrt(num)

rootfunc(16)


"""
Find all the propreties in math package 
"""
everything_math = dir(math)

print everything_math


"""
On Beyond String
"""

def biggest_number(*args):
	print "Max num of ", args
	print max(args)
    	return max(args)
    
def smallest_number(*args):
    	print "Min num of ", args
	print min(args)
    	return min(args)

def distance_from_zero(arg):
    	print " Distance from zero ", arg
	print abs(arg)
    	return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-198)


"""

Get type of variable

"""


print type(89)
print type(90.98)
print type([1, 2, 3])
print type("TEST")










