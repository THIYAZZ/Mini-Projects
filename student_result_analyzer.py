# Student Result Analyzer

def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 80:
        grade = "A"
        result = "Pass"
    elif average >= 60:
        grade = "B"
        result = "Pass"
    elif average >= 40:
        grade = "C"
        result = "Pass"
    else:
        grade = "F"
        result = "Fail"

    return total, average, grade, result


# Main Program
student_name = input("Enter Student Name: ")

marks = []
subjects = ["Maths", "Science", "English", "Computer", "Social"]

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

total, average, grade, result = calculate_result(marks)

print("\n----- Student Result -----")
print("Name      :", student_name)
print("Total     :", total)
print("Average   :", average)
print("Grade     :", grade)
print("Result    :", result)
