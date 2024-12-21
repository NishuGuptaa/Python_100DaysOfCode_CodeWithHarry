def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks!")
    return mfx
@greet
def hello():
    print("Hello World")
@greet
def add(a, b):
    print(a+b)
hello()
# greet(hello)()
# greet(add)(1, 2)
add(1, 2)