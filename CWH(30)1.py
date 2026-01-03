# Fibonacci series

def fibonacci(m):
    a, b = 0, 1
    for i in range(m):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter number of terms: "))
fibonacci(num)