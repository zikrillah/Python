cars = 100
space_in_a_car = 4.0
drivers = 30
passenggers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenggers_per_car = passenggers / cars_driven

print "There are", cars, "cars avaliable."
print "There are only", drivers, "drivers avaliable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passenggers, "to carpool today."
print "We need to put about", average_passenggers_per_car, "in each car."
