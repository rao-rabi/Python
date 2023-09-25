# 3. Write a program that calculates the energy needed to heat water from an initial temperature to a final temperature. Your program should prompt the user to enter the amount of water in kilograms and the initial and final temperatures of the water. The
# formula to compute the energy
# Q = M ∗ (finalTemperature – initialTemperature) ∗ 4184
# where M is the weight of water in kilograms, temperatures are in degrees Celsius,and
# energy Q is measured in joules.


Amount_of_water = int(input("Write amount of water in kilograms: "))
int_temprature = int(input("Write initial temprature in celcius: "))
fin_temprature = int(input("Write final temprature in celcius: "))

Energy = Amount_of_water * (fin_temprature - int_temprature) * 4184

print(f"The Energy required to heat water is: {Energy} Joules")