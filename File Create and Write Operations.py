filename = "student_data.txt"

# Write
with open(filename, "w") as f:
    f.write("Name: Devansh Gupta\n")
    f.write("Roll: 011\n")
    f.write("Subject: PPS\n")
    f.write("Department: CSE\n")

print(f"Data written to '{filename}' successfully.")

# Read back
print(f"\nContents of '{filename}':")

with open(filename, "r") as f:
    print(f.read())