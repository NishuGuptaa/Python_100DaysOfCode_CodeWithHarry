l = [3, 5, 6, "Hi", True, 45, 76, 0, 99]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

print(l[-3])
print(l[len(l)-3])
print(l[5-3])
print(l[2])

if 7 in l:
    print("Yes")
else:
    print("No")

if "i" in "Hi":
    print("Yes")
else:
    print("No")

print(l)
print(l[:]) # [0:lenght of l]
print(l[1:-1])
print(l[1:6])
print(l[1:6:2])

# List Comprehension
lst = [ i for i in range(4)]
print([lst])

lst = [ i*i for i in range(4)]
print([lst])

lst = [ i for i in range(10) if i%2==0]
print([lst])

# List Methods
m = [11, 45, 1, 2, 3, 4, 1, 1]
print(m)
print(m.index(1)) # This method returns the index of the first occurence of the list item.
print(m.count(1))
n = m.copy()
n[0] = 0
print(m)
m.append(7)
print(m)
m.sort()
print(m)
m.sort(reverse=True)
print(m)
m.reverse()
print(m)
m.insert(1, 899)
print(m)
o = [400, 500, 600]
m.extend(o)
print(m)
o = [400, 500, 600]
m.extend(o)
# k = m + o
# print(k)