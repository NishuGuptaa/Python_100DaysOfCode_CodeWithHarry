'''
1 for snake
-1 for water
0 for gun
'''
# import random
# computer = random.choice([-1, 0, 1])
# youstr = input("Enter your choice (s for Snake, g for Gun, w for Water):")
# youDict = {"s":1, "w":-1, "g":0}
# reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
# you = youDict[youstr]

# print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# if(computer == you):
#     print("Its a draw")
# else:
#     if(computer == -1 and you == 1):
#         print("You win!")
#     elif(computer == 1 and you == -1):
#         print("You lose!")
#     elif(computer == -1 and you == 0):
#         print("You lose!")
#     elif(computer == 0 and you == -1):
#         print("You win!")
#     elif(computer == 1 and you == 0):
#         print("You win!")
#     elif(computer == 0 and you == 1):
#         print("You lose!")
#     else:
#         print("Something went wrong!")


import random

def check(comp, user):
    if comp == user:
        return 0
    
    if(comp == -1 and user == 1):
        return 1
    elif(comp == 1 and user == -1):
        return -1
    elif(comp == -1 and user == 0):
        return -1
    elif(comp == 0 and user == -1):
        return 1
    elif(comp == 1 and user == 0):
        return 1
    elif(comp == 0 and user == 1):
        return -1
    


comp = random.randint(-1, 1)
user = int(input("Enter your choice (1 for Snake, 0 for Gun, -1 for Water):"))

score = check(comp, user)

print("You: ", user)
print("Comp: ", comp)

if(score == 0):
    print("Its a draw")
elif(score == -1):
    print("You Lose")
elif(score == 1):
    print("You Win")
else:
    print("Something went wrong!")