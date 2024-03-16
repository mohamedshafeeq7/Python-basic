def is_buzz_number(num):
    return num % 7 == 0 or num % 10 == 7

num = int(input("Enter a number: "))
if is_buzz_number(num):
    print("Buzz Number")
else:
    print("Not a Buzz Number")
