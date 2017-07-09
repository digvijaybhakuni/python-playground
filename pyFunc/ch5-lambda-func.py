"""
Applying  lambda with filter method
"""
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)


"""
Applying  lambda with filter method with condination
"""
squares = [x ** 2 for x in range(1, 10)]
print filter(lambda x: x >= 30 and x <= 70, squares)


movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print movies.items()

for x in movies.items():
    print x[0] , x[1]

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

print threes_and_fives


garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message


garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message
