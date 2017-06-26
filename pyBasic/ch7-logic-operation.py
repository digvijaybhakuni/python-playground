#!python

bool_1 = True and False 

print "Result should be false  : ", bool_1


bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100**0.5 >= 50 or False

bool_four = True or True

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 +1


# Using NOT Operation 

bool_one = not True
print bool_one # Should be False
bool_two = not 3**4 < 4**3
print bool_two # Should be True
bool_three = not 10 % 3 <= 10 % 2
print bool_three # Should be True
bool_four = not 3**2 + 4**2 != 5**2
print bool_four # Should be True
bool_five = not not False
print bool_one # Should be False


#  This and That (or This, But Not That!)

bool_one = False or not True and True
print bool_one
bool_two = False and not True or True
print bool_two
bool_three = True and not (False or False)
print bool_three
bool_four = not not True or False and not True
print bool_four
bool_five = False or not (True and True)
print bool_five

# Mix 'n' Match

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = ( 33 > 23 ) or 'Digvijay' == "Diggu"

# Make me false!
bool_three = not True and 24 - 34 < 0

# Make me true!
bool_four = 12 != 13 and not False 

# Make me true!
bool_five = not True == False 



