def swap(x, y):
    return y, x

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"Before swap: a = {a}, b = {b}")

a, b = swap(a, b)

print(f"After  swap: a = {a}, b = {b}")