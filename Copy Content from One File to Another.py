source = "student_data.txt"
dest = "student_data_copy.txt"

try:
    with open(source, "r") as src, open(dest, "w") as dst:
        content = src.read()
        dst.write(content)

    print(f"File '{source}' copied to '{dest}' successfully.")

    print(f"\nContents of '{dest}':")

    with open(dest, "r") as f:
        print(f.read())

except FileNotFoundError:
    print(f"Source file '{source}' not found. Run Experiment 26 first.")