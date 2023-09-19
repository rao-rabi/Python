# an easy and comprehensive way to write python

# list comprehension

ls = [i for i in range(100) if i%3==0]
print(ls)

# dictionary comprehension

dict1 = {i:f"item {i}"  for i in range(10) if i%2==0}
print(dict1)

# reversing dictionary
dict2 = {i:f"item {i}"  for i in range(20) if i%2==0}
dict2 = {value:key for key,value in dict2.items()}
print(dict2)

# generator comprehensions

gens = (i for i in range(100) if i%2==0)
# print(type(gens))
# print(gens)
# print(gens.__next__())
for i in gens:
    print(i)
  
    
# create a program which ask user his choice and create comprehension according to it.

elem_input = input("Enter a list elements separated by space? ")
List = elem_input.split()

choice = input("""
Which type of comprehension you want to create?
a.List COmprehension
b.Dictionary Comprehension
c.Generator Comprehension
d.Set Comprehension
> """).lower()

if choice == "a":
    lsc = [i for i in List]
    print(type(lsc))
    print(lsc)
elif choice == "b":
    dsc = {i: f"item {i}" for i in List}
    print(type(dsc))
    print(dsc)
elif choice =="c":
    gsc = (i for i in List)
    print(type(gsc))
    print(gsc)
elif choice == "d":
    sec = {i for i in List}
    print(type(sec))
    print(set(sec))
else:
    print('Invalid Choice')