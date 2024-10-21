import string

input_string = input("Введіть текст: ")
words = input_string.split()
word_count = len(words)

if words:
    longest_word = max(words, key = len)
else:
    longest_word = None
    
print(f"Кількість слів: {word_count}")
if longest_word:
    print(f"Найдовше слово: {longest_word}")
else:
    print("Рядок не містить слів")

