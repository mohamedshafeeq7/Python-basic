def print_even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

# Example usage:
start_num = int(input("Enter the start number: "))
end_num = int(input("Enter the end number: "))
print("Even numbers between", start_num, "and", end_num, "are:")
print_even_numbers(start_num, end_num)
