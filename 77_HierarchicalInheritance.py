class BaseClass:
    def base_method(self):
        print("Method from BaseClass")

class D1(BaseClass):
    def d1_method(self):
        print("Method from D1")

class D2(BaseClass):
    def d2_method(self):
        print("Method from D2")

obj1 = D1()
obj2 = D2()

obj1.base_method()
obj1.d1_method()

obj2.base_method()
obj2.d2_method()
