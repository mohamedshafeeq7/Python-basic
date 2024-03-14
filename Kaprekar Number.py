def is_kaprekar_number(num):
    square = str(num ** 2)
    for i in range(len(square)):
        left, right = int(square[:i] or 0), int(square[i:] or 0)
        if left + right == num and left != 0 and right != 0:
            return True
    return False

num = int(input("Enter a number: "))
if is_kaprekar_number(num):
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")
