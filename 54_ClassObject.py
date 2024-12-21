class Person:
    name = "Hemant"
    occupation = "SDE"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
a.name = "Shubh"
a.occupation = "HR"
# print(a.name, a.occupation)
a.info()
b.info()