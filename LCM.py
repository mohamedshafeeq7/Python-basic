def find_lcm(x, y):
    lcm = max(x, y)
    while True:
        if lcm % x == 0 and lcm % y == 0:
            return lcm
        lcm += 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lcm = find_lcm(num1, num2)
print("LCM of", num1, "and", num2, ":", lcm)
