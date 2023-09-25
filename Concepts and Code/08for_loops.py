# for loops iterate through elements of any iterable

for item in ["Rao Rabi", "Ali", "Ahmad", "Nasir", "Umer", "Zohaib"]:
    print(item)
 
  
# print numbers in a range
for num in range(0,20,2):
    print(num)

# add amount of prices in a list

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total price is {total}")