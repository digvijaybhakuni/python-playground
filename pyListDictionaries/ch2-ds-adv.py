doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

print doubles_by_3


even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]

print even_squares

cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0 ]

print cubes_by_four

"""
List Slicing Syntax
[start:end:stride]
"""
l = [i ** 2 for i in range(1, 11)]

print l[2:9:2]

"""
Omitting Indices
Use list slicing to print out every odd element of my_list from start to finish.
"""
my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2]


"""
Reversing a List
"""
my_list = range(1, 11)

backwards = my_list[::-1]

print backwards


"""
Reversing a List
by 10
"""
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

"""
more comrpi
"""
to_21 = range(1, 22)
odds = to_21[::2]
print odds
middle_third = to_21[7:14]
print middle_third