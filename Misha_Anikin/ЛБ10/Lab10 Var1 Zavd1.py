import string

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
text = text.lower()
translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator)
words = clean_text.split()
unique_words = set(words)
sorted_unique_words = sorted(unique_words)

with open('output.txt', 'w', encoding='utf-8') as output_file:
    for word in sorted_unique_words:
        output_file.write(word + '\n')
        
print(f"Кількість оригінальних слів: {len(sorted_unique_words)}")