## Logical Operators
# and ---> if both are true
# or ----> if any of both is true
# not ---> converts false to true and vice versa

has_good_credit = True
has_criminal_record = False

if has_good_credit and has_criminal_record:
    print("You are not eligible for this loan")
elif has_good_credit and not has_criminal_record:
    print("you are eligible for this loan")
else :
    print("you are not eligible for this loan")
    


## Comparison Operators

name = input("What is Your name? ")
if len(name) < 3:
    print('Your name must be atleast 3 Characters long.')
elif len(name) > 50:
    print ('your name cannot exceed more than 50 characters.')
else:
    print("name looks good!")