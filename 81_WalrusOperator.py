a = True
print(a := False)

num = [1, 2, 3, 4, 5]
while(n := len(num)) > 0:
    print(num.pop())

happy = True
print(happy)
print(happy := True)


# foods = list()
# while True:
#     food = input("What food do you like?")
#     if food == 'quit':
#         break
#     foods.append(food)

foods = list()
while(food := input("What food do you like?: ")) != "quit":
    foods.append(food)