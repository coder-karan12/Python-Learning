# String Formating
country = "India"
name = "Karry"
print(f"Hey my name is {name}! and i am from {country}")
print(f"We use fstring like this :Hey my name is {{name}}! and i am from {{country}}")

price = 49.09999
txt = f"For only {price:.2f} dollars!" #.2f is used to get only 2 deicmal values
print(txt)

print(f"{2 * 30}")

print(type(f"{2 * 30}"))
