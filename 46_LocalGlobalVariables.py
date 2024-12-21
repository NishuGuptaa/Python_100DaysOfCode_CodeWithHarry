# x = 4
# print(x)
# def hello():
#     x = 5
#     print(f"The local x is {x}")
#     print("Hello")
# print(f"The global x is {x}")
# hello()
# x = 5
# print(f"The global x is {x}")


x = 10
def my_function():
    global x
    x = 4
    y = 5
    print(y)
my_function()
print(x)