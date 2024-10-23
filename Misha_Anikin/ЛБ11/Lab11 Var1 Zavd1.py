import csv

def save_students_to_csv(students, filename="students.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Прізвище", "Рік народження"])
        for surname, birth_year in students.items():
            writer.writerow([surname, birth_year])
    print(f"Дані успішно збережено в файл {filename}")
    
def read_students_from_csv(filename="students.csv"):
    students = {}
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                surname, birth_year = row
                students[surname] = birth_year
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    return students

students_data = {
    "Aнікін": "2006",
    "Бутенко": "2007",
    "Салаєва": "2005",
    "Селінний": "2007",
    "Переверзєв": "1991"
    }

save_students_to_csv(students_data)

loaded_students = read_students_from_csv()
print("Зчитані дані:", loaded_students)