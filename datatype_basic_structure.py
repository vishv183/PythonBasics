""""
library -  It is a reusable chunk of code that we can use by importing it into our program
Example of libraries are matplotlib, pytorch and pygame
Package - It is a collection of modules
Example of  packages are numpy and pandas
"""
# data types  int, float, str - String
name = str('xyz')

"""
List Methods 
S.no	Method	Description
1	append()	Used for adding elements to the end of the List. 
2	copy()	It returns a shallow copy of a list
3	clear()	This method is used for removing all items from the list. 
4	count()	These methods count the elements.
5	extend()	Adds each element of an iterable to the end of the List
6	index()	Returns the lowest index where the element appears. 
7	insert()	Inserts a given element at a given index in a list. 
8	pop()	Removes and returns the last value from the List or the given index value.
9	remove()	Removes a given object from the List. 
10	reverse()	Reverses objects of the List in place.
11	sort()	Sort a List in ascending, descending, or user-defined order
12	min()	Calculates the minimum of all the elements of the List
13	max()	Calculates the maximum of all the elements of the List 
"""

num = [1, 2, 3, 4, 45, 5, 66, 3]
print(f'type of  num is {type(num)}')
# using in built list function
name = ['rahul', 'om', 'tim']
print(f'type of name is {type(name)}')
# accessing specific  element in the list
print(f'second  element of list is {name[1]}')
#slicing
print(f'using slicing : {num[2:5]}, {num[:5]}')
#count method of list
print(f'number  of  element  in list is  {num.count(3)}')
#insert
name.insert(1, "aryan")
print(name)
#append
name.append("tom")
print(name)
#remove
name.remove("tom")
print(name)

"""
Dictionary methods 
Method	        Description
dict.clear()	Remove all the elements from the dictionary
dict.copy()	    Returns a copy of the dictionary
dict.get(key, default = “None”)	 Returns the value of specified key
dict.items()	 Returns a list containing a tuple for each key value pair
dict.keys()	 Returns a list containing dictionary’s keys
dict.update(dict2)	Updates dictionary with specified key-value pairs
dict.values()	 Returns a list of all the values of dictionary
pop()	 Remove the element with specified key
popItem()	Removes the last inserted key-value pair
 dict.setdefault(key,default= “None”)	set the key to the default value if the key is not specified in the dictionary
dict.has_key(key)	returns true if the dictionary contains the specified key.

"""
coding_languages = {
    1: "python",
    2: "c++",
    3: "go",
    4: "R"
}
# uisng  dict function
person = dict(name="John", age=30, city="New York")
print(person)
print(f'coding languages = {coding_languages}')
# dict keys method
print(f'coding languages dictonary keys = {coding_languages.keys()}')
# dict values method
print(f'coding languages dictonary values = {coding_languages.values()}')
print(person)
#pop item method
person.popitem()
print(person)
# pop method
print(f'Before using pop method  in dictonary : {coding_languages}')
print(f" using pop method of dictonary = {coding_languages.pop(3)}")
print(f'After using pop method  in dictonary : {coding_languages}')
"""
capitalize() - Converts the first character of the string to a capital (uppercase) letter
casefold() - Implements caseless string matching
center(width[, fillchar]) - Pad the string with the specified character.
count(sub[, start[, end]]) - Returns the number of occurrences of a substring in the string.
encode(encoding="utf-8", errors="strict") - Encodes strings with the specified encoding scheme
endswith(suffix[, start[, end]]) - Returns “True” if a string ends with the given suffix
expandtabs(tabsize=8) - Specifies the amount of space to be substituted with the “\t” symbol in the string
find(sub[, start[, end]]) - Returns the lowest index of the substring if it is found
format(*args, **kwargs) - Formats the string for printing it to console
format_map(mapping) - Formats specified values in a string using a dictionary
index(sub[, start[, end]]) - Returns the position of the first occurrence of a substring in a string
isalnum() - Checks whether all the characters in a given string are alphanumeric or not
isalpha() - Returns “True” if all characters in the string are alphabets
isdecimal() - Returns true if all characters in a string are decimal
isdigit() - Returns “True” if all characters in the string are digits
isidentifier() - Check whether a string is a valid identifier or not
islower() - Checks if all characters in the string are lowercase
isnumeric() - Returns “True” if all characters in the string are numeric characters
isprintable() - Returns “True” if all characters in the string are printable or the string is empty
isspace() - Returns “True” if all characters in the string are whitespace characters
istitle() - Returns “True” if the string is a title cased string
isupper() - Checks if all characters in the string are uppercase
join(iterable) - Returns a concatenated String
ljust(width[, fillchar]) - Left aligns the string according to the width specified
lower() - Converts all uppercase characters in a string into lowercase
lstrip([chars]) - Returns the string with leading characters removed
maketrans(x[, y[, z]]) - Returns a translation table
partition(sep) - Splits the string at the first occurrence of the separator
replace(old, new[, count]) - Replaces all occurrences of a substring with another substring
rfind(sub[, start[, end]]) - Returns the highest index of the substring
rindex(sub[, start[, end]]) - Returns the highest index of the substring inside the string
rjust(width[, fillchar]) - Right aligns the string according to the width specified
rpartition(sep) - Split the given string into three parts
rsplit([sep[, maxsplit]]) - Split the string from the right by the specified separator
rstrip([chars]) - Removes trailing characters
splitlines([keepends]) - Split the lines at line boundaries
startswith(prefix[, start[, end]]) - Returns “True” if a string starts with the given prefix
strip([chars]) - Returns the string with both leading and trailing characters
swapcase() - Converts all uppercase characters to lowercase and vice versa
title() - Convert string to title case
translate(table) - Modify string according to given translation mappings
upper() - Converts all lowercase characters in a string into uppercase
zfill(width) - Returns a copy of the string with ‘0’ characters padded to the left side of the string
"""
# Declaring String
subject = str("maths")
name = str("vishv")
print(f'using upper method in string {name.upper()}')
print(f'using upper method in string {name.capitalize()}')
print(f'orignal string :  {name} Accessing  character of an string :  {name[2]}')

"""
Types of Control Flow in Python

Python If Statement
Python If Else Statement
Python Nested If Statement
Python Elif
Ternary Statement | Short Hand If Else Statement
"""
# if else
a = 5
b = 6
if (a == b):
    print(f'a is similar to b ')
else:
    print('a is not similar to b')

# nested if

i = 10
if (i == 10):
    if (i < 15):
        print("i is smaller than 15")
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

"""
How to use the for loop in Python
Python For Loop Syntax
Python For Loop with String
Python For Loop with Integer
Python for loop Enumerate
Nested For Loops in Python
Python For Loop with List
Python For Loop with Dictionary
Python For Loop with Tuple
Python For Loop with Zip()
"""

#syntax of  for loop

for i in range(10):
    print(i)

# Implementing for loop
list1 = [1, 2, 3, 4, 5]
list2 = [x for x in list1 if x % 2 == 0]

# nested for loop
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

# For Loop with List
i=0
no = [1, 2, 33, 4, 4, 5, 5, 66, 7, 7]
size = len(no)
for i in range(size):
    print(f'{no[i]}')

# For Loop with Dictionary
# Iterating over dictionary
print("Dictionary Iteration")

coding_languages = {
    1: "python",
    2: "c++",
    3: "go",
    4: "R"
}
i=0
print(coding_languages)
for key, value in coding_languages.items():
    print(f"Key: {key}, Value: {value}")
# zip()
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)
i = 0
target="cherry"
for i in range(len(fruits)):
    if fruits[i] == target:
        print(f'found in index {i}')
