# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Hello")
#         super().parent_method()
#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        # self.name = name
        # self.id = id
        self.lang = lang

hemant = Employee("Hemant", "400")
shubh = Programmer("Shubh", "500", "Python")
print(shubh.name)
print(shubh.id)
print(shubh.lang)