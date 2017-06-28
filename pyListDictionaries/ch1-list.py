

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

"""
Replace in Place
"""

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
zoo_animals[3] = "sloth"



"""
Lenght and append
"""

suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("watch")
suitcase.append("shoes")
suitcase.append("pants")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

"""
List  Slicing
"""

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]  # The last two items (index four and five)

print first
print middle
print last


"""
Slicings Lists and String
"""

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals[6:]   # From the seventh character to the end


"""
Maintaining Orders
"""

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

animals.insert(duck_index, "cobra")


print animals # Observe what prints after the insert operation


"""
For One and all
"""

my_list = [1,9,3,8,5,7]

for number in my_list:
    print number, " = ", number * 2   


"""
More with 'For'
"""


start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
    square_list.append(x ** 2)

square_list.sort()

start_list.sort()
print start_list
print square_list

"""
How to remove
"""
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']


backpack.remove("dagger")

