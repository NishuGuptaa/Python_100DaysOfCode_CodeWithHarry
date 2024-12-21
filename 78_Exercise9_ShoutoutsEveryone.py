# Write a program to pronounce list of names using win32 API.
# If you are given list l as follows:
# l = ['John', 'Mary', 'David', 'Emma']
# Your program should pronounce:
# Shoutout to John
# Shoutout to Mary
# Shoutout to David
# Shoutout to Emma

# from os import system
# names = ['John', 'Mary', 'David', 'Emma']
# for name in names:
#     system(f"say {name}")

import win32com.client
names = ['John', 'Mary', 'David', 'Emma']

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in names:
    text = f"Shoutout to {name}"
    print(text) 
    speaker.Speak(text)
