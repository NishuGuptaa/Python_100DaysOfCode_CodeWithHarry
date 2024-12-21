class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e = Employee('Hemant', 14000)
print(e.name)
print(e.salary)
string = "Shubh-18000"
e1 = Employee.fromStr(string)
print(e1.name)
print(e1.salary)