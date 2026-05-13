subjects = 5
total = 0
for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for Subject {i} (out of 100): "))
    total += marks
percentage = total / subjects
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"
print(f"Total      : {total:.2f}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")