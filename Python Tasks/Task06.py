# 6. Write a program that prompts the user to enter three integers and displays them in increasing order.

num_1 = int(input("Enter number 1: "))
num_3 = int(input("Enter number 3: "))
num_2 = int(input("Enter number 2: "))

list = []

list.append(num_1)
list.append(num_2)
list.append(num_3)

list.sort()
for num in list:
    print(num)