# Q6: Grade Calculator
# This program asks the user for marks in 5 subjects (out of 100 each).
# It calculates total marks, percentage, grade, and pass/fail result.
#
# Logic:
# - total_marks = sum of all 5 subject marks
# - percentage = (total_marks / 500) * 100
# - grade is decided based on percentage using given scale
# - pass if all subjects >= 40, else fail
#
# Mathematics behind it:
# - Each subject max = 100, so total max = 500
# - percentage = (total_marks / 500) * 100
# - grade scale:
#   90-100 = A+
#   80-89 = A
#   70-79 = B
#   60-69 = C
#   50-59 = D
#   below 50 = F
# - pass condition: every subject mark >= 40

def grade_calculator():
    # Step 1: Ask user for marks in 5 subjects
    marks = []
    for i in range(1, 6):
        score = int(input(f"Enter marks for subject {i} (out of 100): "))
        marks.append(score)

    # Step 2: Calculate total marks
    total_marks = sum(marks)

    # Step 3: Calculate percentage
    percentage = (total_marks / 500) * 100

    # Step 4: Decide grade based on percentage
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    # Step 5: Check pass/fail condition
    if all(score >= 40 for score in marks):
        result = "PASS"
    else:
        result = "FAIL"

    # Step 6: Show results
    print("\n=== GRADE CALCULATOR RESULTS ===")
    for i, score in enumerate(marks, start=1):
        print(f"Subject {i}: {score}")
    print(f"Total Marks: {total_marks} / 500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")

# Step 7: Run the function
grade_calculator()
