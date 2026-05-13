n = int(input("Enter number of rows: "))

print("\n-- Right-angle Triangle --")
for i in range(1, n + 1):
    print("*" * i)

print("\n-- Inverted Triangle --")
for i in range(n, 0, -1):
    print("*" * i)

print("\n-- Number Triangle --")
for i in range(1, n + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))