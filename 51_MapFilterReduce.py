l = [1, 2, 4, 6, 4, 3]
# Map
# def cube(x):
#     return x*x*x
# print(cube(2))

# newl = []
# for item in l:
#     newl.append(cube(item))
newl = list(map(lambda x: x*x*x, l))
print(newl)

# Filter
def filter_function(a):
    return a>2
newll = list(filter(filter_function, l))
print(newll)

# Reduce
from functools import reduce
num = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x+y, num)
print(sum)