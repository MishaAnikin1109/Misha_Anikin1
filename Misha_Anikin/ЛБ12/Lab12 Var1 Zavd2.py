def remove_extra_spaces(text):
    return ' '.join(text.split())

with open("input.txt", "r") as file:
    text = file.read()
    
cleaned_text = remove_extra_spaces(text)

with open("output.txt", "w") as file:
    file.write(cleaned_text)
    
print("Зайві пробіли видалено, очищений текст збережено в output.txt")