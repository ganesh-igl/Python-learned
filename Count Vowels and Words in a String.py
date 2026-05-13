line = input("Enter a line of text: ")

vowels = sum(1 for ch in line.lower() if ch in "aeiou")
words = len(line.split())

print(f"Vowel count : {vowels}")
print(f"Word count  : {words}")