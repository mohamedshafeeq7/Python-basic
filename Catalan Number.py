def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

def is_catalan_number(num):
    if num < 0:
        return False
    for i in range(num + 1):
        if binomial_coefficient(2 * i, i) == num:
            return True
    return False

num = int(input("Enter a number: "))
if is_catalan_number(num):
    print("Catalan Number")
else:
    print("Not a Catalan Number")
