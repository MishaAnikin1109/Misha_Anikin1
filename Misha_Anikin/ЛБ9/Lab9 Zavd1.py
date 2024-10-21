students = [
    ("Михайло", 18, 79.2),
    ("Аліна", 19, 94.0),
    ("Дмитро", 17, 57.8),
    ("Сергій", 33, 85.1)
]

def display_students(students):
    print("Список студентів:")
    for student in students:
        name, age, average_grade = student
        print(f"Ім'я: {name}, Вік: {age}, Середній бал: {average_grade}")

def calculate_average_grade(students):
    total_grade = sum(student[2] for student in students)
    return total_grade / len(students)

display_students(students)

average_grade = calculate_average_grade(students)
print(f"\nСередній бал групи: {average_grade:.2f}")