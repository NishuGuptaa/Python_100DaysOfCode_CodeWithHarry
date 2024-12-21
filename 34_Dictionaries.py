dic = {
    "Hemant": "Human Being",
    "Spoon": "Object",
    "Apple": "Fruit"
}
print(dic)
print(dic["Apple"])
# print(dic["Apple1"]) # It shows error
print(dic.get("Apple1"))

dic1 = {
    1: "Hemant",
    2: "Raman",
    3: "Neha",
    4: "Shubh"
}
print(dic1[3])
print(dic1.keys())
print(dic1.values())
for key in dic1.keys():
    print(dic1[key])

print(dic1.items())
for key, value in dic1.items():
    print(key)
    print(value)

# Dictionary Methods
ep1 = {122:45, 123:89, 567:78, 670:78}
ep2 = {222:67, 566:99}

# ep1.update(ep2)
# print(ep1)

# ep1.clear()
# print(ep1)

# empt = {}
# print(empt)

# ep1.pop(122)
# print(ep1)

# ep1.popitem()
# print(ep1)

# del ep1
# print(ep1)

# del ep1[122]
# print(ep1)