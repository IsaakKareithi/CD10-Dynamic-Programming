def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
# example usage
n = int(input("Enter number to get its factorial: "))
result = factorial_recursive(n)
print(f"the factorial of {n} is: {result}")