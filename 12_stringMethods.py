# Strings are immutable
a = "!!Hemant! !!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Hemant","Jarvis"))
print(a.split(" "))
blogHeading = "introduction TO jS"
print(blogHeading.capitalize())
print(a.count("Hemant"))

str1 = "Welcome to the Console !!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))
print(str1.endswith("?"))
print(str1.endswith("to",4,10))
print(str1.find("is"))
str2 = "WelcomeToTheConsole"
print(str1.isalnum())
print(str2.isalnum())
str3 = "  "
print(str3.isspace())
str4 = "World Health Organization"
print(str4.istitle())
print(str1.istitle())
print(str1.startswith("Welcome"))
print(str1.swapcase())
print(str1.title())
