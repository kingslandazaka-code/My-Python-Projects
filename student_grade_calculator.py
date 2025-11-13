# === Student Grade Calculator ===

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

def grade_calculator():
    print("=== Student Grade Calculator ===")
    subjects = ["Math", "English", "Science"]
    total = 0
    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        total += mark

    average = total / len(subjects)
    grade = calculate_grade(average)
    print("Average:", average)
    print("Grade:", grade)

grade_calculator()
