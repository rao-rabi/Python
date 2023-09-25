# 4. Write a program that reads an integer between 0 and 1000 and adds all the digits in
# the integer. For example, if an integer is 932, the sum of all its digits is 14.
# (Hint: Use the % operator to extract digits, and use the // operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 // 10 = 93.)

number = int(input("Enter the number between 0 and 1000: "))

if 0 <= number <= 1000:
    total = 0
    
    while number > 0:
        digit = number % 10
        
        total += digit
    
        number = number // 10
        
    print(total)
else:
    print("Invalid Number")