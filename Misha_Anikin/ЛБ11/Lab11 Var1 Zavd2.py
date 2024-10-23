import json

def save_books_to_json(books, filename="books.json"):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
    print(f"Дані успішно збережено в файл {filename}")
    
def input_books():
    books = []
    while True:
        title = input("Введіть назву книги (або 'stop' для завершення): ")
        if title.lower() == 'stop':
            break
        author = input("Введіть автора книги: ")
        books.append({"Назва": title, "Автор": author})
    return books

books_data = input_books()

save_books_to_json(books_data)