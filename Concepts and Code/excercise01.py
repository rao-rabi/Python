#Write a program which converts weight in kg's to pounds and pounds to kg's on the basis of user input.

weight = int(input("Enter Your weight? "))
ask_unit = input("(L)bs or (K)g? ")

if ask_unit.lower() == 'l':
    weight *= 0.45
    print(f"Your weight is: {weight} kg")
else:
    weight /=0.45
    print(f"Your weight is: {weight} pounds")
    