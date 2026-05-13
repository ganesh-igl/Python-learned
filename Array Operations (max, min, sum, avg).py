n = int(input("Enter number of elements: "))

arr = [int(input(f"Element {i+1}: ")) for i in range(n)]

print(f"Array   : {arr}")
print(f"Maximum : {max(arr)}")
print(f"Minimum : {min(arr)}")
print(f"Sum     : {sum(arr)}")
print(f"Average : {sum(arr)/len(arr):.2f}")