# creating an (x,y) pair using nested loop

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")


# create an F shape of stars using nested loops.  

numbers = [5,2,5,2,2]

for star in numbers:
    output = ""
    for count in range(star):
        output += "x"
    print(output)
