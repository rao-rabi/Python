names = ["Rao Rabi", "Ali", "Ahmad", "Umer", "Zohaib", "Nasir"]
print(names[2:])
print(names[:])
print(names[5])
print(names[-4])
print(names)

names[0] = "Rabi Khan"

print(names)

# find the largest number in a list.

numbers = [45, 21, 41, 9, 123, 56, 67]
max = numbers[0]

for num in numbers:
    if num > max:
        max = num
print(f"largest number in the list is: {max}")


# nested lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# access to a single elem
numl = matrix[2][0]
print(numl)
# using nested loop to print matrix
for row in matrix:
    for item in row:
        print(item)

first_name = ["BlueRay ", "Upchuck ", "Lojack ", "Gizmo ", "Do-Rag"]
last_name = ["Zzz", "Burp", "Dogbone", "Droop"]
full_name = []
for a_first_name in first_name:
    for a_last_name in last_name:
        full_name.append(f"{a_first_name} {a_last_name}")
print(full_name)

# list methods

nums = [2, 4, 6, 43, 90, 4, 53, 67, 4]
l2 = ["a", "b", "c", "d"]

# add an elem at last
nums.append(34)
print(nums)

# copy list
nums2 = nums.copy()
print(nums2)

# insert an elem at any index
nums.insert(3, 300)
print(nums)

# to sort list
nums.sort()
print(nums)

# to reverse list
nums.reverse()
print(nums)

# to find index of any elem
i = nums.index(43)
print(i)

# to remove any elem
nums.remove(300)
print(nums)

# to count occurences of any elem
c = nums.count(4)
print(c)

# to remove elem at any index
nums.pop(5)
print(nums)

# remove from one list and append it to other one
print(l2)
l2.append(nums.pop())
print(l2)

# to clear the whole list elems
nums.clear()
print(nums)

# write a program to remove duplicates from a list

l3 = [2, 45, 67, 2, 12, 67, 2, 6]
unique = []

for item in l3:
    if item not in unique:
        unique.append(item)
print(unique)

# dictionaries inside list

customers = [
    {
        "customer id": 0,
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    {
        "customer id": 1,
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    {
        "customer id": 2,
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
]

customer_to_find = customers[1]
print(customer_to_find["address"])

#add a new dictionary

new_customer_id = len(customers)

new_dictionary = {
    "customer id": new_customer_id,
    "first name": "nick",
    "last name": "bell",
    "address": "3 Main notingam.",
}

customers.append(new_dictionary)
print(customers)
