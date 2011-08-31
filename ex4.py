cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capactiy = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capactiy, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."


# Traceback (most recent call last):
# File "ex4.py", line 8, in <module>
# average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not define
#
# This error was caused by referencing a variable that does not exist. 
# car_pool_capacity should have been carpool_capacity on line 8

# Using 4.0 instead of 4 forces python to use floating point numbers instead of integers.

# A floating point number is a representation of a number that can contain a fraction part. (3.4, 5.7 81.2334 are examples)
# The point in a floating point number can move (hence float) as there is no fixed number of digits before or after the point. 
