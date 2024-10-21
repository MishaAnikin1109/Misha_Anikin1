student1_subjects = {"математика", "фізика", "інформатика"}
student2_subjects = {"хімія", "інформатика", "біологія"}

def display_subjects(student_subjects, student_name):
    print(f"Предмети {student_name}: {', '.join(student_subjects)}")

common_subjects = student1_subjects.intersection(student2_subjects)

unique_to_student1 = student1_subjects.difference(student2_subjects)

all_subjects = student1_subjects.union(student2_subjects)

display_subjects(student1_subjects, "студента 1")
display_subjects(student2_subjects, "студента 2")
print(f"\nЗагальні предмети: {', '.join(common_subjects)}")
print(f"Предмети, які вивчає тільки студент 1: {', '.join(unique_to_student1)}")
print(f"Всі предмети: {', '.join(all_subjects)}")