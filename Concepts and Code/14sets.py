# a set has unique numbers only

numbers  = [1,1,2,3,4]
first = set(numbers)

second = {1,5}

print(first)
# union
print(first | second)

#intersection
print(first & second)

#difference
print(first - second)

#print uncommon
print(first ^ second)

# check existance
if 2 in first:
    print("yes")
else:
    print("no")
