s = input("Enter a string: ").replace(" ", "").lower()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")