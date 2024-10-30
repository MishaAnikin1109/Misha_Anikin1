class Telephone:
    def __init__(self1, number, model):
        self1.number = number
        self1.model = model
        self1.incoming_calls = []
        
    def call(self1, caller_name, caller_number):
        self1.incoming_calls.append((caller_name, caller_number))
        print(f"Вхідний дзвінок від {caller_name} ({caller_number}) на номер {self1.number}")
        
    def delete_call(self1):
        if self1.incoming_calls:
            removed_call = self1.incoming_calls.pop()
            print(f"Видалено дзвінок від {removed_call[0]} ({removed_call[1]})")
        else:
            print("Немає вхідних дзвінків для видалення")
            
    def show_info(self1):
        print(f"Модель: {self1.model}, Номер: {self1.number}")
        print("Історія вхідних дзвінків:")
        for call in self1.incoming_calls:
            print(f"- {call[0]} ({call[1]})")