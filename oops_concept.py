"""
Functions
The main types of functions in Python are:

Built-in function
User-defined function
Lambda functions
Recursive functions
"""
import re
import math
from abc import ABC, abstractmethod

#using builtin function
x = 5
print(f'The factorial of 5 is : {math.factorial(x)}')


def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


"""
Exception Handling 
"""
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")


def fun(a):
    if a < 4:
        b = a / (a - 3)
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

"""
    Regex Functions     
Function	Description
re.findall()	finds and returns all matching occurrences in a list
re.compile() 	Regular expressions are compiled into pattern objects
re.split() 	Split string by the occurrences of a character or a pattern.
re.sub() 	Replaces all occurrences of a character or patter with a replacement string.
re.escape()	Escapes special character
re.search()	Searches for first occurrence of character or pattern
"""

# using  compile function of regex
pattern = re.compile("^[A-Z]+$")
# using  search  function of regex
print(pattern.search("HELLO WoRLD"))
string = "Hello World!"
pattern = r"World!$"
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")
# using findall function
pattern = r"[aeiou]"
text = "hello"
result = re.findall(pattern, text)
print(result)
"""
class 
"""


class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def bonus(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus
        final_salary = salary + bonus
        print(final_salary)
        return final_salary


e1 = Employee(name="xyz", position="abc", salary=100000.000)
e1.bonus(salary=e1.salary, bonus=100)


# multiple inheritance
class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    @staticmethod
    def m():
        print("In Class4")


obj = Class2()
obj.m()
Class4.m()

# Class2.m(obj)
# Class3.m(obj)
# Class1.m(obj)

"""
Decorator  
types of decorator
class decorator and function decorator 
"""


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


def abc(*args, **kwargs):
    print(a, b)


abc(6, 5)


# implementing  encapsulation

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary


employee = Employee('John Doe', 30, 50000)

print(employee.get_name())

print(employee.get_age())

print(employee.get_salary())

employee.set_salary(60000)

print(employee.get_salary())


# abstraction class

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def printDetails(self):
        print("  ok ")

    # Create concrete method
    def accelerate(self):
        print("speed up ...")

    def break_applied(self):
        print("Car stop")


class Hatchback(Car):

    def printDetails(self):
        print("Brand:", self.brand);
        print("Model:", self.model);
        print("Year:", self.year);

    def Sunroof(self):
        print("Not having this feature")


class Suv(Car):

    def printDetails(self):
        print("Brand:", self.brand);
        print("Model:", self.model);
        print("Year:", self.year);

    def Sunroof(self):
        print("Available")


car1 = Hatchback("Maruti", "Alto", "2022");

car1.printDetails()
car1.accelerate()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        print(12345566)

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

# Create a circle and a square
circle = Circle()
square = Square()

# Draw the circle and the square
circle.draw()
square.draw()