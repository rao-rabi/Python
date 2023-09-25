# 2. Write a program that converts pounds into kilograms. The program prompts the user to enter a value in pounds, converts it to kilograms, and displays the result. One pound is 0.454 kilograms.

pounds = input("Enter weight in pounds: ")

kilograms = int(pounds) * 0.454

print(f"Weight In Kilograms is: {kilograms}")