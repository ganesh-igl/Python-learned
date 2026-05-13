n = int(input("Enter an integer: "))

sign = -1 if n < 0 else 1
reversed_n = int(str(abs(n))[::-1]) * sign

print(f"Reversed number: {reversed_n}")