original_list = [1, 2, 3, 4, 5, 6]

print("Original")
print(*original_list)

print("Reversed")
print(
    *reversed(original_list)
)  # this return iterator that yield items in reverse order this is not a list

print("Reverse")
original_list.reverse()  # this return None and reverse order of items in the list
print(*original_list)


""" combine two list """

list1 = ["a", "b", "c"]

list2 = ["e", "f", "g"]

list3 = list1 + list2

print(list3)  # in this we are mising 'd' how to add it in between

# this will result in error
# list3 = list1 + 'd' + list2

list3 = [*list1, "d", *list2]  ## *list is called value unpacking
print(list3)


v1, v2, *v3 = original_list

print(v1, v2, v3)  # 6 5 [4,3,2,1]


v1, *v2, v3 = original_list

print(v1, v2, v3)  # 6 [5,4,3,2] 1


sum_list = [2, 4, 6]


def sum_it(a, b, c):
    return a + b + c


print(sum_it(*sum_list))

print(sum_list[-1:])  # get last value
print(sum_list[:-1])  # get all except last
print(sum_list[1:])  # get all except fist
print(sum_list[:1])  # get fist value
print(original_list[1:3])  # get between 1 and 2 (include 1, exclude 3)
print(original_list[2:-1])  # get between 2 and -1 (include 2, exclude -1) -1 repr last

print("sum_list reversed")
print(sum_list[::-1])

from functools import reduce


def sum_all(*args):
    return reduce(lambda x, y: x + y, args)


print(sum_all(1, 2, 3, 4, 5))
print(sum_all(*sum_list))



sum_map = {'a': 1, 'b': 2 , 'c': 3}


print(sum_it(**sum_map)) # this is unpacking to kwargs a=1, b=2, c=3


p1 = {'name': 'Digvijay'}
p2 = {'job': 'Programmer'}

# p3 = p1 + p2 # not possible result in error dict + dict operation 
p3 = {**p1, **p2}
print(p3) # dict will merge into one


p3 = {**p1, **p2, "age": "33"}
print(p3) # dict will merge into one with added key for age



def my_func(**kwargs):
    for key, val in kwargs.items():
        print(f" {key} : {val}")


my_func(**p3)

print("kwargs params")

my_func(lang='Python', version=3.10)
