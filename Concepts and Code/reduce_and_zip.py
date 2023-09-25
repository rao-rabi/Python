# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along

from functools import reduce

list_1 = [1,4,5,3,9,34,32]

num = reduce(lambda x,y:x+y, list_1)
mul = reduce(lambda x,y:x*y, list_1)
div = reduce(lambda x,y:x/y, list_1)
print(num)
print(mul)
print(div)

# zip() method takes iterable containers and returns a single iterator object, having mapped values from all the containers. 

tup1 = ("Rao Rabi", "Rana Ali", "Ahmad")

tup2 = (21,25,19)

res = list(zip(tup1, tup2))
print(res)
res = set(zip(tup1, tup2))
print(res)
res = dict(zip(tup1, tup2))
print(res)
