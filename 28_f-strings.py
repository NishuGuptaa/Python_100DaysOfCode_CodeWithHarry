letter = 'Hey my name is {} and I am from {}'
country = "India"
name = "Hemant"
print(letter.format(name, country))
print(f"Hey my name is {name} and I am from {country}")

letter = 'Hey my name is {1} and I am from {0}'
country = "India"
name = "Hemant"
print(letter.format(country, name))

price = 49.09999
txt = f"For only {price:2f} dollars!"
print(txt)

print((f"{2*4}"))
print(type(f"{2*4}"))