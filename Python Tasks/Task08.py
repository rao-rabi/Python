# 8. Write a program that prompts the user to enter a point (x, y) and checks whether the point is within the circle centered at
# (0, 0) with radius 10. For example, (4, 5) is inside the circle and (9, 9) is outside the circle, as shown in the given Figure.
# (Hint: A point is in the circle if its distance to (0, 0) is less than or equal to 10. The formula for computing the distance is
# A(x ! − x " ) ! + (y ! − y " ) ! . Test your program to cover all cases.)
# Two sample runs are shown next.

import math
x = int(input("Enter x-coordinate of the point: ")) 
y = int(input("Enter y-coordinate of the point: ")) 

distance = math.sqrt(x**2 + y**2)

if distance <= 10:
    print(f"The point ({x}, {y}) is inside the circle within radius 10")
else:
    print(f"The point ({x}, {y}) is outside the circle")