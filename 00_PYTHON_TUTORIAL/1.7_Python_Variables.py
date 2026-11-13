# 1 Python Variables

# A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

# In Python, variables do not need to be declared with any particular `type`, and can even change type after they have been set.

x = 4       # x is of type int
print(x)
x = "Sally" # x is now of type str
print(x)

# 1.2 Casting

# If you come from JAVA and want to specify the `data type` of a variable, this can be done with casting.

x = str(3)    # x will be '3'
print(x)
y = int(3)    # y will be 3
print(y)
z = float(3)  # z will be 3.0
print(z)

# 1.3 Get type.
# If you come from JAVA and want to specify the `data type` of a variable, this can be done with casting.

print("x is type", type(x))
print("y is type", type(y))
print("z is type", type(z))

# 1.4. Single or Double Quotes?
x = "John" # Mostly used
# is the same as
x = 'John'

# 1.5. Case-Sensitive variables
a = 4
print(a)
A = "Sally"
print(A)
#A will not overwrite a. They are TWO different variables.
age = 3
Age = 4
AGE = 5
print(age)
print(Age)
print(AGE)

## 2.1. Variable Names

"""
- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
- Rules for Python variables:
  - A variable name must start with a letter or the underscore character
  - A variable name cannot start with a number
  - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
  - Variable names are case-sensitive (age, Age and AGE are three different variables)
  - A variable name cannot be any of the Python keywords.
"""

# Goog variable names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Bad varialble names

2myvar = "John"
my-var = "John"
my var = "John"

# 2.2. Multi Words Variable Names

# 2.2.1. Camel Case
myVariableName = "John"

# 2.2.2. Pascal Case
MyVariableName = "John"

# 2.2.3. Snake Case
my_variable_name = "John"

# 3. Python Variables - Assign Multiple Values

# 3.1. Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# 3.2. One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# 3.3. Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# 4. Python - Output Variables
# 4.1. Output Variables
x = "Python is awesome"
print(x)

# Separate output variables with commas
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Separate output variables with commas
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)

# Math operations inside Output
x = 5
y = 10
print(x + y)

# Output different data types, separated with '+'
x = 5
y = "John"
print(x + y)

# Output different data types, separated with comma
x = 5
y = "John"
print(x, y)

# 5. Python - Global Variables
# 5.1. Global Variables, before functions.

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Local variables, inside functions.
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

# 'global' keyword, promotes a variable from LOCAL to GLOBAL
x = "awesome"
print("Original value of 'x' was:", x)

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)



