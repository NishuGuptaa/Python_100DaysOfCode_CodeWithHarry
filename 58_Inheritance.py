class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

e = Employee("Shubh Das", 450)
e.showDetails()
e1 = Programmer("Hemant", 480)
e1.showDetails()
e1.showLanguage()