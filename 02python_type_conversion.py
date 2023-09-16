user_weight = input("Enter your weight in pounds: ")
print(type(user_weight))
# explicit conversion(manual conversion)
weight_in_kg = int(user_weight) * 0.45
# implict conversion(automatic conversion)
print("Your weight in Kg is: ", weight_in_kg)
print(type(weight_in_kg))

# ord()---> used to convert char to int

s = "a"
c = ord(s)
print(c)

# hex()----> convert int to hexadecimal str

n = 32;
m = hex(n)
print(m)

# oct()----> convert int to octal str

u = 32;
v = oct(u)
print(v)