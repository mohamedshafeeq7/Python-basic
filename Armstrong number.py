def is_armstrong(number):
    # Convert number to string to count digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Example usage:
input_number = int(input("Enter a number: "))
if is_armstrong(input_number):
    print(input_number, "is an Armstrong number.")
else:
    print(input_number, "is not an Armstrong number.")
