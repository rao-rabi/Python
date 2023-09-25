# 5. Given an airplane’s acceleration a and takeoff speed v, you can compute the minimum runway length needed for an airplane to take off using the following formula:
# length = v square / 2 a
# Write a program that prompts the user to enter v in meters/second (m/s) and the
# Acceleration a in meters/second squared (m/s 2 ) and displays the minimum runway
# length.

speed = int(input("Enter speed in m/s: "))
acceleration = int(input("Enter acceleration in m/s²: "))

length = (speed ** 2) / (2* acceleration)

print(f"The minimum runway length needed to take off is {length} meters")