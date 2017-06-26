def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

print shut_down("no")


"""
Import and use
"""

from math import sqrt 

print sqrt(13689)


"""
Distance from zero if its int or float
"""

def distance_from_zero(var):
    return abs(var) if type(var) == int or type(var) == float else "Nope"


print distance_from_zero(45678)

