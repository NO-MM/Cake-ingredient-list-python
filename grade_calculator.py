# Grade Calculator

# User input
student_name = input("Enter your name: ")
cat_score = float(input("Enter mark for Computer Application Technology(CAT): "))
it_score = float(input("Enter mark for Information Technology (IT): "))
math_score = float(input("Enter mark for Mathematics: "))

# Calculate average
average = (cat_score + it_score + math_score) / 3

# Determine grade
if average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 50:
    grade = 'D'
elif average >= 40:
    grade = 'E'
else:
    grade = 'F'
    
# Status Passed/Failed
status = "Passed" if average >= 50 else "Failed"

# Output results
print("\n--- Result ---")
print(f"Profile: {student_name}")
print(f"Average Mark: {average:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")
