def find_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
hcf = find_hcf(num1, num2)
print("HCF of", num1, "and", num2, ":", hcf)
