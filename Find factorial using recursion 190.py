def factorial(n):
    if num == 0 or num == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter the number: "))
if num > 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of", num, "is", factorial(num))