names  = ["Kukki", "Diggu"] 

for n in names:
	print n



webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for k in webster:
    print k, " > ", webster[k]




a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for n in a:
    if n % 2 == 0:
        print n




def fizz_count(lst):
    count = 0;
    for s in lst:
        if s == "fizz":
            count = count + 1
    return count
    

print fizz_count(["fizz","cat","fizz"])

# Looping and calcute

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for i in food:
        if stock[i] > 0:
            total = total + prices[i]
            stock[i] = stock[i] - 1
    return total


print compute_bill(shopping_list)
    
    


