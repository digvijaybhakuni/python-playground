def hotel_cost(nights):
    return nights * 140
    
def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475


print plane_ride_cost("Tampa")

def rental_car_cost(days):
    total_cost = days * 40
    if days >= 7:
        return total_cost - 50
    elif days >= 3:
        return total_cost - 20
    else:
        return total_cost
    
    
rental_car_cost(12)

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
    
print trip_cost("Tampa", 5, 888)
