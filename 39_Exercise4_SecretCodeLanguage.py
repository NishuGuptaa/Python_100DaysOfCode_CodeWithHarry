# Write a python program to translate a message into secret code Language. 
# Use the rules below to translate normal English into secret code language
# Coding:if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:simply reverse the string
# Decoding:if the word contains less than 3 characters, reverse it
# else:remove 3 random characters from start and end. Now remove the last Letter and append it to the beginning

import random
import string

def generate_random_string(length=3):
    return ''.join(random.choices(string.ascii_letters, k=length))

st = input("Enter message: ")
words = st.split(" ")
coding = int(input("Enter 1 for Coding or 0 for Decoding: "))

if coding == 1:  # Encoding
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = generate_random_string()
            r2 = generate_random_string()
            nwords.append(r1 + word[1:] + word[0] + r2)
        else:
            nwords.append(word[::-1])
    print("Encoded message:", " ".join(nwords))

elif coding == 0:  # Decoding
    nwords = []
    for word in words:
        if len(word) >= 6:  # Minimum length to include random strings
            stnew = word[3:-3]  # Remove random strings
            stnew = stnew[-1] + stnew[:-1]  # Reverse the encoding logic
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("Decoded message:", " ".join(nwords))

else:
    print("Invalid choice. Please enter 1 for Coding or 0 for Decoding.")
