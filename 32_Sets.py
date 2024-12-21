s = {2, 4, 2, 6, False, "Hemant"}
print(s)

for value in s:
    print(value)

# Set Methods
s1 = {1, 2, 5, 6}
s2 = {3, 6, 9}
print(s1.union(s2))
print(s1, s2)

# s1.update(s2)
# print(s1, s2)

# s3 = s1.intersection(s2)
# print(s3)

# s1.intersection_update(s2)
# print(s1)

# s3 = s1.symmetric_difference(s2)
# print(s3)

# print(s1.isdisjoint(s2))

# print(s1.issuperset(s2))

# print(s1.issubset(s2))

# s2.add(100)
# print(s2)

# s2.remove(9)
# print(s2)

# s2.remove(10) # It shows error 
# s2.discard(10) # does not show error
# print(s2)

# s3 = s1.pop() # Random value pop
# print(s3)

# del s2
# print(s2)

# s2.clear()
# print(s2)