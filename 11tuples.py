# tuples are immutable we can't modify them

tup = (1,2,3,4,2,52,6)

print(tup[3])

#methods

# count existance of an elem
c = tup.count(2)
print(c)

# to get index of any elem

b = tup.index(52)
print(b)

# unpacking for lists and tuples

tup1 = (1,2,3)
x, y ,z =tup1
print(x * y * z)