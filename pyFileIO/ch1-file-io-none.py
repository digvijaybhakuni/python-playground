my_file = open("output.txt", "r+") 
# w for write mode, r+ for read/write, r for read
my_list = [i**2 for i in range(1,11)]

for x in my_list:
    my_file.write(str(x) + "\n")
    
my_file.close()

my_file = open("output.txt", "r")

print my_file.read()

my_file.close()


# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print read_file.read()
read_file.close()

