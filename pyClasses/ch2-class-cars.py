class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
        
    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

print my_car.condition
print my_car.drive_car()
print my_car.condition

print my_car.display_car()


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg 
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

print my_car.condition
print my_car.drive_car()
print my_car.condition



class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
        

my_point = Point3D(x=1, y=2, z=3)
print my_point