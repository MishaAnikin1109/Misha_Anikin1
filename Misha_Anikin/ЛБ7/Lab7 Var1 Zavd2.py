import string

def transform_middle_letters(s):
    length = len(s)
    mid_index = length // 2
    return s[:mid_index - 1] + s[mid_index -1:mid_index + 1].upper() + s[mid_index + 1:]

N = int(input("Введіть кількість рядків: "))
lines = []

for _ in range(N):
    line = input("Введіть рядок (парна довжина): ")
    if len(line) % 2 != 0:
        print("Рядок має бути парної довжини!")
        continue
    lines.append(line)
    
for line in lines:
    transformed_line = transform_middle_letters(line)
    print(transformed_line)