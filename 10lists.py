names = ["Rao Rabi", "Ali","Ahmad","Umer","Zohaib","Nasir"]
print(names[2:])
print(names[:])
print(names[5])
print(names[-4])
print(names)

names[0] = "Rabi Khan"

print(names)

# find the largest number in a list.

numbers = [45,21,41,9,123,56,67]
max = numbers[0]

for num in numbers:
    if(num > max):       
        max = num
print(f"largest number in the list is: {max}")   


# nested lists

matrix  = [
    [1, 2, 3],
    [4 ,5, 6],
    [7, 8, 9]
]
# access to a single elem
numl = matrix [2] [0]
print(numl)
# using nested loop to print matrix
for row in matrix:
    for item in row:
        print(item)
        
        