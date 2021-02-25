def using_control_once():
    if False != True:
        return "Success #1"

def using_control_again():
    if not 33 == 22:
        return "Success #2"

print using_control_once()
print using_control_again()

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns False

select = raw_input("Press 1 for Black Knight or 2 for French soldier ? ")

if(select == '1'):
	print black_knight()
elif (select == '2'):
	print french_soldier()
else:
	print select, 'Is not a vaild choice'




def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


# Make sure that the_flying_circus() returns True
def the_flying_circus(num):
    if not num != 23:
	print "Num is equal 23" 
        return True
    elif num < 56:
	print "Num is less then 56"
        return True
    elif num > 32 and num < 109:
	print "Num is grt 32 and lst 109"
        return True
    else:
        return True

num = int(raw_input("Enter a num "))
print the_flying_circus(num)



