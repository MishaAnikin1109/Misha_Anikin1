import random

N = int(input("Введіть розмір матриці N: "))
matrix = [[random.randint(1, 12) for _ in range(N)] for _ in range(N)]
print("Згенерована матриця: ")
for row in matrix:
    print(row)
    
product = 1
for i in range(N):
    product *= matrix[i][i]
print(f"\nДобуток елементів на головній діагоналі: {product}")
unique_elements = set()

for i in range(N):
    for j in range(N):
        if matrix[i][j] in unique_elements:
            matrix[i][j] = 0
        else:
            unique_elements.add(matrix[i][j])
            
print("\nМатриця після видалення повторів: ")
for row in matrix:
    print(row)