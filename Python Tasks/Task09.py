# 9. Write a program that prompts the user to enter a three-digit integer and determines
# whether it is a palindrome number. A number is a palindrome if it reads the same from
# right to left and from left to right.

num = input("Enter a 3 digit number: ")

if(len(num) == 3):
    if (num == num[::-1]):
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")    
   
else:
    print('Number should be 3 digit')
    

