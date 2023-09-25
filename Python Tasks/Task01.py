# 1. Assume a runner runs 14 kilometers in 45 minutes and 30 seconds. Write a program that displays the average speed in miles per hour. (Note that 1 mile is 1.6 kilometers.)

kilometers = 14

# speed_in_miles = d_in_km / time

miles_per_km = 1/1.6

time_to_hours = (45 / 60) + (30 / 3600)

miles = kilometers * miles_per_km

speed = miles / time_to_hours

print(f"Speed is {speed} mph")