# Error handling in python
try:
    a = int(input("Enter Password: "))
    if a == 1234:
        print("Succesfully Login")
    else:
        print("Incorrect Password try again")

except ValueError:
    print("Password Contains only numbers")