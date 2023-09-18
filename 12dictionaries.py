customer = {
    "Name": "Rao Rabi",
    "age" : 30,
    "is_verified" : True,
}

print(customer)

print(customer.get("age"))  #if not present prevents error and return none or defult value get("key", "default value")

# update or modify value
customer["age"] = 21
print(customer)

# adding new key,value pair 
customer["Date of Birth"] = "17 July 2003"
print(customer)

# deleting a pair
del customer["is_verified"]
print(customer)

# write a program to convert 1234 to one two three four

phone = input("Enter numbers: ")

digits_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# write a program to convert symbols to emojis

message = input("> ")
words = message.split(" ")

emojis = {
    ":)": "😄",
    ":(": "😥",
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)

# to print keys and values
city = {
    "lhr": 500000,
    "fsd": 200000,
    "kar": 300000,
}

for c in city.keys():
    print(c) 

for c in city.values():
    print(c) 
    
for key,value in city.items():
    k = key
    v = str(value) 
    print("The " + k + " has " + v + " Population.")


# list inside a dictionary and dictionary inside dictionary

customers = {
   0: {
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
        "discounts": ["brother in law","standard","volume","loyalty"]
    },
   1: {
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
        "discounts": ["brother in law","standard","volume","loyalty"]
    },
   2: {
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
        "discounts": ["brother in law","standard","volume","loyalty"]
    },
}

# print(customers[1])
# print(customers[1]["address"])

id = int(input("Enter Customer Id: "))
package = input("Enter your package: ")
customers[id]["discounts"] = [package]

price = 3000

discount = customers[id]["discounts"]

if "brother in law" in discount:
    price = price - (price *.30)
elif "standard" in discount:
    price = price - (price *.20)
elif "volume" in discount:
    price = price - (price *.10)
elif "loyalty" in discount:
    price = price - (price *.15)
else:
    price = price
print(f"""{customers[id]["first name"]} {customers[id]["last name"]}'s price after discount is: {price}""")
    
