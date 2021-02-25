# Animal Class
class Animal(object):
    """Makes cute animals."""
    health = "good"
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        print self.name
        print self.age

    def nobody(self):
        pass
        

hippo  = Animal("A1", 78)
sloth  = Animal("A2", 12)
ocelot = Animal("A3", 23)


print hippo.health
print sloth.health
print ocelot.health


class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."


my_cart = ShoppingCart("Test")

my_cart.add_item("Item 1", 34)



# Inheritance Customer is base class of ReturningCustomer

class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()



# Shape Class
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Triangle class
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.number_of_sides = 3


    
tri = Triangle(1, 2, 4)

print tri.number_of_sides


class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12
        
    def full_time_wage(self, hours):
        print self.employee_name, "is PTE"
        return super(PartTimeEmployee, self).calculate_wage(hours)
        

milton = PartTimeEmployee("Milton")
print milton.calculate_wage(10)
print milton.full_time_wage(12)


print PartTimeEmployee("DG").calculate_wage(12)
print Employee("DG").calculate_wage(12)


# Triangle Class extend object
class Triangle(object):
    number_of_sides = 3
    # init 
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    def check_angles(self):
        return True if self.sumAngle() == 180 else False
    
    def sumAngle(self):
        return self.angle1 + self.angle2 + self.angle3


triangle = Triangle(60, 60, 60)
print triangle.number_of_sides
print triangle.check_angles()

class Equilateral(Triangle):
    angle = 60
    
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle 


new_triangle = Equilateral()
print "New Triangle (Equilateral)"
print new_triangle.number_of_sides
print new_triangle.check_angles()
