n = int(input("Enter number of elements: "))

arr = [int(input(f"Element {i+1}: ")) for i in range(n)]

print(f"Before sorting: {arr}")

# Bubble sort (mirrors the C approach)
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(f"After sorting : {arr}")