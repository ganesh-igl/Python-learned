r = int(input("Rows   : "))
c = int(input("Columns: "))

matrix = [[int(input(f"  [{i+1}][{j+1}]: ")) for j in range(c)] for i in range(r)]

print("\nOriginal Matrix:")
for row in matrix:
    print("  " + "  ".join(f"{v:4}" for v in row))

transpose = [[matrix[i][j] for i in range(r)] for j in range(c)]

print("\nTranspose Matrix:")
for row in transpose:
    print("  " + "  ".join(f"{v:4}" for v in row))