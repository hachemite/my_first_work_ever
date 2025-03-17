cars = 100
space_in_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers  # cars_not_driven = 100-30 = 70
cars_driven = drivers #cars_driven = 30
carpool_capacity = cars_driven * space_in_car    #سعة مرافقة = carpool_capacity =120  
average_passengers_per_car = passengers / cars_driven #متوسط الركاب لكل سيارة = average_passengers_per_car = 3.0


print("there are " , cars ,"cars available. ")
print("there are only " , drivers , "drivers available. ")
print("there will be " , cars_not_driven ,"empty cars today .")
print("We can transport", carpool_capacity ,"people today.")
print("We have " , passengers, "to carpool today .")
print("We need to put about ", average_passengers_per_car , "in each car.")



#it is regular average_passengers_per_car is passengers / cars_driven ,because all cars have a  4 space without is 3 can the car transport
#and for carpool capacity it is just the person in car with driver and passengers is 120