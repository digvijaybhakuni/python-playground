"""
You may not know this, but file objects contain 
a special pair of built-in methods: __enter__() and __exit__(). 
The details aren't important, but what is important is that 
when a file object's __exit__() method is invoked, 
it automatically closes the file. 
How do we invoke this method? With 'with' and 'as'.
"""

with open("text.txt", "w") as textfile:
	textfile.write("Success!")

with open("text.txt", "w") as my_file:
    my_file.write("My Name is Digvijay Singh Bhakuni")

if not my_file.closed:
    my_file.close()
    
print my_file.closed


with open("output.txt", "r") as my_file:
    for line in my_file:
        print line,
    print 