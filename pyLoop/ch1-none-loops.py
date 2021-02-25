
# Simple While

count = 0

if count < 9:
    print "Hello, I am an if statement and count is", count
    
while count <= 9:
    print "Hello, I am a while and count is", count
    count += 1



num = 1

while num <= 10:  # Fill in the condition
        print num ** 2
        num += 1



choice = raw_input('Enjoying the course? (y/n)')

while choice != "y" and choice != "n":  # Fill in the condition (before the colon)
        choice = raw_input("Sorry, I didn't catch that. Enter again: ")



# While / Else 

import random

count = 3
while count > 0:
        num = random.randint(1, 6)
        print num
        if num == 5:
            print "Sorry, you lose!"
            break
        count -= 1
else:
    print "You win!"



"""
print with out end line,
swap A or a with X
"""

phrase = "A bird in the hand..."

# Add your for loop
for w in phrase:
    if w == "A" or w == "a":
        print "X",
    else:
        print w,


#Don't delete this print statement!
print


