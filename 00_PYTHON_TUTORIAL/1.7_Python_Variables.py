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

# If you come from JAVA and want to specify the `data type` of a variable, this can be done with casting.

print("x is type", type(x))
print("y is type", type(y))
print("z is type", type(z))