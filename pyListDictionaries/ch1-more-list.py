
n = [2, 3, 4, 5]

def list_extender(lst):
    lst.append(9)
    return lst

print list_extender(n)

# range use 



print "range(9) -> ", range(9) 
print "range(9, 20) -> ", range(9, 20) 
print "range(9, 30, 4) -> ", range(9, 30, 4) 




# Range to itrate over list



def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print double_list(n)


def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(0, 3))


def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result = result + numbers[i]
    return result

print total(n)


ns = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for i in range(len(words)):
        result = result + words[i]
    return result

# 


m = [1, 2, 3]
n = [4, 5, 6]

print join_strings(ns)


def join_lists(a, b):
    return a + b




print join_lists(m, n)



lists_ns = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

# Add your function here
def flatten(lists):
    results = []
    for l in lists:
        for n in l:
            results.append(n)
    
    return results



print flatten(lists_ns)

