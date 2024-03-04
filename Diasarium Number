def is_disarium_number(num):
    sum_of_powers = sum(int(digit) ** (index + 1) for index, digit in enumerate(str(num)))
    return sum_of_powers == num

num = int(input("Enter a number: "))
if is_disarium_number(num):
    print("Disarium Number")
else:
    print("Not a Disarium Number")
