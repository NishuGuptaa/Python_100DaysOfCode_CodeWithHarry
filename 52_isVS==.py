a = 4
b = "4"
print(a is b) # exact location of object in memory
print(a == b) # value

a = [1, 2, 43]
b = [1, 2, 43]
print(a is b)
print(a == b)

a = 3
b = 3
print(a is b)
print(a == b)

a = (1, 2)
b = (1, 2)
print(a is b)
print(a == b)

a = None
b = None
print(a is b)
print(a is None)
print(a == b)