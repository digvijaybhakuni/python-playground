

def tax(bill):
    print """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    print """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)



""" 
square of number
"""

def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    

square(10)



def power(base, exponent):
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(2,4)



"""
This by_three method return cube of number 
if it is divisable by three else false 
"""

def cube(number):
    return number ** 3


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


print by_three(99)




