class Book:
    def __init__(self1, title, author, publisher, year, pages):
        self1.title = title
        self1.author = author
        self1.publisher = publisher
        self1.year = year
        self1.pages = pages
        
    def update_year(self1, new_year):
        self.year = new_year
        
    def update_pages(self1, new_pages):
        self.pages = new_pages
        
    def __str__(self1):
        return f"Назва: {self1.title}, Автор: {self1.author}, Видавництво: {self1.publisher}, Рік: {self1.year}, Сторінки: {self1.pages}"
    
book_list = []

def add_book(book_list):
    title = input("Введіть назву книги: ")
    author = input("Введіть автора книги: ")
    publisher = input("Введіть видавництво: ")
    year = int(input("Введіть рік видання: "))
    pages = int(input("Введіть кількість сторінок: "))
    
    book = Book(title, author, publisher, year, pages)
    book_list.append(book)
    print("\nКнигу додано до списку.")
    
def remove_book(book_list, title):
    for book in book_list:
        if book.title == title:
            book_list.remove(book)
            print("\nКнига з такою назвою не знайдена.")
            
while True:
    print("\n1. Додати нову книгу")
    print("2. Вилучити книгу")
    print("3. Показати всі книги")
    print("4. Вийти")
    
    choice = input("Виберіть дію: ")
    if choice == "1":
        add_book(book_list)
    elif choice == "2":
        title = input("Введіть назву книги, яку хочете вилучити: ")
        remove_book(book_list, title)
    elif choice == "3":
        if not book_list:
            print("\nСписок книг порожній.")
        else:
            print("\nСписок книг")
            for book in book_list:
                print(book)
    elif choice == "4":
        break
    else:
        print("\nНеправильний вибір. Спробуйте ще раз.")