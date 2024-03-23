def is_neon_number(num):
    square = num * num
    sum_of_digits = sum(int(digit) for digit in str(square))
    return sum_of_digits == num

num = int(input("Enter a number: "))
if is_neon_number(num):
    print("Neon Number")
else:
    print("Not a Neon Number")
