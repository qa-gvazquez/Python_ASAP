# Python Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

# INT

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# FLOAT
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# FLOAT with powers of 10
x = 35e3
y = 12E4
z = -87.7e100
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

# COMPLEX

x = 3+5j
y = 5j
z = -5j

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print("x = ",x)
print(type(x))
print("y = ",y)
print(type(y))
print("z = ",z)
print(type(z))

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(z)

print("a is now float of x with value", a, "and type", type(a))
print("b is now int of y with value", b, "and type", type(b))
print("c is now complex of z with value", c, "and type", type(c))