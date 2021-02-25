
def is_even(x):
    return True if x % 2 == 0 else False

print "is_even(23)", is_even(23)

def is_int(x):
    return True if x == round(x) else False

print "is_int(2.2) ",is_int(2.2)
print "is_int(2.0) ",is_int(2.0)
print "is_int(2) ",is_int(2)

def digit_sum(x):
    sum = 0
    while x >= 1:
        sum += x % 10
        x = x / 10
    return sum
    

print "digit_sum(232) ", digit_sum(232)



def factorial(x):
    fac = 1
    while x > 1:
        fac = fac * x
        x -= 1
    return fac

print "factorial(89) ", factorial(89)

def factorial_rc(x):
    if x > 1:
        return x * factorial_rc(x -1)
    else:
        return 1
print "factorial_rc(4) ", factorial_rc(4)

def is_prime(x):
    if x < 2 :
        return False
    n = 2
    while n < x:
        if x % n == 0:
            return False
        n += 1
    return True

print "is_prime(57)", is_prime(57)


def reverse_com(text):
    return text[::-1]

print reverse_com("Diggu")


def reverse_fun(text):
    return reversed(text)

print reverse_fun("Diggu")


def reverse(text):
    str = ""
    ctr = len(text)-1 
    while ctr >= 0:
        str += text[ctr]
        ctr -= 1
    return str

print reverse("Diggu")


def anti_vowel(text):
    new_text = ""
    for x in text:
        if x not in "aeiouAEIOU":
            new_text += x     
    return new_text
    

print anti_vowel("Hey You!")

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
         
def scrabble_score(word):
    score_i = 0
    for x in word:
        score_i += score[x.lower()]
    return score_i
    
print "Digvijay = ", scrabble_score("Digvijay")



def censor(text, word):
    lst_text = []
    words = text.split(" ")
    for x in words:
        if x == word:
            lst_text.append("*" * len(x))
        else:
            lst_text.append(x)
    return " ".join(lst_text)
    
print censor("this hack is wack hack", "hack") 



def count(sequence, item):
    count = 0
    for n in sequence:
        if n == item:
            count += 1
    return count
    
    
print "TES > ", count([1,2,1,1], 1)

def purify(nums):
    return [n for n in nums if n % 2 == 0] 
    
print "TEst >> ", purify([1, 2, 3, 4, 5])


def product(nums):
    return reduce((lambda x, y: x * y), nums)

print product([4, 5, 5])


def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst
    

print remove_duplicates([1,1,2,2]) 


def median(lst):
    lst = sorted(lst)
    print lst
    m = len(lst)/2
    if len(lst) % 2 == 0:
        print m
        print (lst[m - 1] + lst[m])
        return float(lst[m] + lst[m - 1]) / 2.0
    else:
        return lst[m]       
    
print median([4, 5, 5, 4])


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    if len(scores) > 0:
        return reduce((lambda a, b: a + b), scores)
    else:
        return 0
        

def grades_average(scores):
    total = float(grades_sum(scores))
    return total / len(scores) if total > 0 else 0 
    
print grades_average(grades)
