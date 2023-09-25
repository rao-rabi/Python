# syntax for strings
first_name = 'Rao'
last_name = "Rabi"

intro = '''Hy!
 My name is Rao Rabi.'''
print(intro)

# formatted strings

f_name = "john"
l_name = "smith"

name = f'{f_name} + [{l_name}] is a coder'
print(name)

print(name[:])    #to copy full string
print(name[::-1])   #to reverse string
print(name[0:9])   #to slice from string
print(name[2:-2])

# string methods

course = "Python for Beginners"

print(len(course))    #to find length

print(course.upper())  #to convert to uppercase

print(course.lower())  #to convert to lowercase

print(course.replace("Beginners","Programmers"))   #to replace string 

print(course.find("o"))  #to find index of any character

print("python" in course)  #to find any character or substr exists in a string   ?
print("Python" in course)  #to find any character or substr exists in a string

s1 = slice(1,7,2)       #slice method to slice from string
print(course[s1])