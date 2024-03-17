def divide_two_numbers(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero."
    else:
        return num1 / num2

# Example usage:
number1 = float(input("Enter the numerator: "))
number2 = float(input("Enter the denominator: "))
result = divide_two_numbers(number1, number2)
print("The result of dividing the numerator by the denominator is:", result)
