class BaseClass:
    def base_method(self):
        print("Method from BaseClass")

class Derived1(BaseClass):
    def derived1_method(self):
        print("Method from Derived1")

class Derived2(BaseClass):
    def derived2_method(self):
        print("Method from Derived2")

class Derived3(Derived1, Derived2):
    def derived3_method(self):
        print("Method from Derived3")


obj = Derived3()

# obj.base_method()       
# obj.derived1_method()   
# obj.derived2_method()   
obj.derived3_method()   

print(Derived3.mro())
