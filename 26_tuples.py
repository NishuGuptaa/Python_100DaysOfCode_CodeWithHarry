t = (1, 5 , 6, "Hi", True)
print(type(t), t )
print(len(t))

if 6 in t:
    print("Yes")
else:
    print("No")

t2 = t[1:4]
print(t2)

t = (1)
print(type(t), t )
t = (1, )
print(type(t), t )