# class Employee:
#     def __init__(self):
#         self.__name = "Hello"

# a = Employee()
# print(a._Employee__name) # (Name Mangling) Can be accessed indirectly
# # print(a.__name) # Cannot be accessed directly
# print(a.__dir__())


class Student:
    def __init__(self):
        self._name = "Hello"

    def _funName(self):
        return "HI"
    
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))
print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())