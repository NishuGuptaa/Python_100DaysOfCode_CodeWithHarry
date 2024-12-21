import time
# print(4)
# time.sleep(3)
# print("This is printed after 3 seconds")


# def usingWhile():
#     i = 0
#     while i < 500:
#         i = i + 1
#         print(i)

# def usingFor():
#     for i in range(500):
#         print(i)

# init = time.time()
# usingWhile()
# print(time.time() - init)
# init = time.time()
# usingFor()
# print(time.time() - init)


t = time.localtime()
formatted_time = time.strftime("%Y-%M-%D %H:%M:%S", t)
print(formatted_time)