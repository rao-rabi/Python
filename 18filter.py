# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

# return numbers greater than 5 in a list
list_1 = [2,30,4,5,6,10,90]

def search(num):
    return num > 5

print(list(filter(search, list_1)))

# print vowels

def filter_vowels(var):
    letters = ["a","e","i","o","u"]
    if (var in letters):
        return True
    else:
        return False
 
    
sequence = ["a","e","r","t","y","u","h","g","f","i","o","f","s","b"]

# vowels = filter(filter_vowels, sequence)
#     for item in vowels:
#         print(item)

def vowels(item):
    list = ["a","e","i","o","u"]
    if (item in list):
        return True
    else:
        return False;
    

vowel = filter(vowels, sequence)
for item in vowel:
    print("Vowel is :", item )

        