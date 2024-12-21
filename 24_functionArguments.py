def average(a, b): # Here a and b required arguments
    print("The average is ",(a+b)/2)
average(4, 6)

# Default Arguments
def average(a=9, b=1):
    print("The average is ",(a+b)/2)
average()

def average(a=9, b=1): # Ignore a=9 and b=1
    print("The average is ",(a+b)/2)
average(1,5)

def average(a=9, b=1):
    print("The average is ",(a+b)/2)
average(5) # a = 5

def average(a=9, b=1):
    print("The average is ",(a+b)/2)
average(b=9)

# Keyword Arguments
def average(a=9, b=1):
    print("The average is ",(a+b)/2)
average(b=9, a=21)

# Required Arguments
def average(a, b=1):
    print("The average is ",(a+b)/2)
average(a=21)

# Variable Length Arguments
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))
average(5, 6, 7, 1)

# Return Statement
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
c = average(5, 6, 7, 1)
print(c)