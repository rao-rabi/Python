# 10. Write a Python program which accepts a 4 digit binary numbers as its input and check
# if the number is even or not.

def is_even(num):
    return num % 2 == 0; 

binary_number = input("Enter a 4 digit binary number using 0 and 1: ")

if len(binary_number) != 4 or not binary_number.isdigit() or set(binary_number) - {'1','0'}:
    print(f"{binary_number} is not a binary number")
else:
    decimal_number = int(binary_number, 2)
    
    if is_even(decimal_number):
        print(f"{binary_number} is even")
    else:
        print(f"{binary_number} is odd.")