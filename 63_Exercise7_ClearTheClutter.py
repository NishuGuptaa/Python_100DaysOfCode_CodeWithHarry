# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other files formats.

import os
files = os.listdir("clutterFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutterFolder/{file}",f"clutterFolder/{i}.png")
        i = i + 1
