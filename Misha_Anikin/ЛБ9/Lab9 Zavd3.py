students = {
    "Олександр": [85, 95, 78],
    "Марія": [92, 88, 94],
    "Іван": [76, 83, 39],
    "Ольга": [42, 85, 91]
}
def display_grades(students):
    for name, grades in students.items():
        print(f"Оцінки {name}: {', '.join(map(str, grades))}")

def calculate_average(students):
    averages = {}
    for name, grades in students.items():
        averages[name] = sum(grades) / len(grades)
    return averages

def display_averages(averages):
    print("\nСередні бали студентів:")
    for name, average in averages.items():
        print(f"{name}: {average:.2f}")

display_grades(students)
averages = calculate_average(students)
display_averages(averages)