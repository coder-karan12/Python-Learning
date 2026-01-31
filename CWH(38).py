# Custom Errors in Python
a = int(input("Enter Any Value Between 5 and 9: "))

if (a<5 or a<9):
    raise ValueError("Value should be between 5 and 9")


# We use custom error to stop code breaking ahead it some values are incorrect 
# Wrong values can create errors ahead so we can stop that by adding custom errors
