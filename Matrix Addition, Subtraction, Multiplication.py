
def read_matrix(name, rows, cols):
    print(f"Enter {name} ({rows}x{cols}):")
    return [[int(input(f"  [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        print("  " + "  ".join(f"{v:4}" for v in row))

r = int(input("Rows   : "))
c = int(input("Columns: "))

A = read_matrix("Matrix A", r, c)
B = read_matrix("Matrix B", r, c)

print("\nAddition:")
print_matrix([[A[i][j] + B[i][j] for j in range(c)] for i in range(r)])

print("\nSubtraction (A - B):")
print_matrix([[A[i][j] - B[i][j] for j in range(c)] for i in range(r)])

if r == c:      # Square matrices — multiplication supported
    print("\nMultiplication (A x B):")

    result = [
        [sum(A[i][k] * B[k][j] for k in range(r)) for j in range(c)]
        for i in range(r)
    ]

    print_matrix(result)

else:
    print("\nMultiplication skipped (non-square matrix entered).")