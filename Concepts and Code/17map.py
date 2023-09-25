# The map() function executes a specified function for each item in an iterable.


nums = [2,3,4,5,6,6,7,1,8,9]
numsin = list(map(int, nums))

for i in numsin:
    i += 1
    print(i)
    
# print squares
numsq = list(map(lambda x:x*x, nums))

print (numsq)

def square(x):
    return x * x

def cube(x):
    return x * x * x


func = [square, cube]

for i in range(5):
    numsmp = list(map(lambda x:x(i), func))
    print(numsmp)