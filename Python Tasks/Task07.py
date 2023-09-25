# 7. (Compute the perimeter of a triangle) Write a program that reads three edges for a
# triangle and computes the perimeter if the input is valid. Otherwise, display that the
# input is invalid. The input is valid if the sum of every pair of two edges is greater than
# the remaining edge.

edge_1 = float(input("Enter length of first edge: "))
edge_2 = float(input("Enter length of second edge: "))
edge_3 = float(input("Enter length of third edge: "))

if edge_1 + edge_2 > edge_3 and edge_2 + edge_3 > edge_1 and edge_1 and edge_3 > edge_2:
    perimeter  = edge_1 + edge_2 + edge_3
    print(f"Perimeter of triangle is: {perimeter}")
    
else:
    print("Invald Input")