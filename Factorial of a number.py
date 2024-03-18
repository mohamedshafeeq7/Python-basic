def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

# Example usage:
number = int(input("Enter a non-negative integer: "))
result = factorial(number)
print("The factorial of", number, "is:", result)
