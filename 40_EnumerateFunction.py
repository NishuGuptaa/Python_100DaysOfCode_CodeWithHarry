l = [12, 34, 67, 99, 83, 1, 5]
index = 0
for mark in l:
    print(mark)
    if(index==3):
        print("Awesome!")
    index += 1

for index, mark in enumerate(l):
    print(mark)
    if(index==3):
        print("Awesome!")