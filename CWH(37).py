# Finally Keyword in python
try:
    l = [1,5,6,7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred")

finally:
    print("I am always executed")

# Finally block always exwcutes. whether there is error or not, it will always be executed
