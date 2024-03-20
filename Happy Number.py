def is_happy_number(num):
    seen = set()
    while num != 1:
        num = sum(int(digit) ** 2 for digit in str(num))
        if num in seen:
            return False
        seen.add(num)
    return True

num = int(input("Enter a number: "))
if is_happy_number(num):
    print("Happy Number")
else:
    print("Not a Happy Number")
