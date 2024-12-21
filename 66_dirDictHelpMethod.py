# dir
print("DIR")
x = [1, 2, 3]
print(dir(x))
print(x.__add__)

x = (1, 2, 3)
print(dir(x))

# dict
print("DICT")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("Hemant", 20)
print(p.__dict__)

print("HELP")
print(help(str))
print(help(Person))