
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