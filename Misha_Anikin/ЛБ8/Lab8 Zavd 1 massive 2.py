import numpy as np

matrix = np.array([[2, 9, 15], [7, 3, 1], [0, 6, 34]])
print("Початковий двовимірний масив: ")
print(matrix)

matrix_plus_one = matrix + 1
print("\nМатриця після додавання 1 до кожного елемента: ")
print(matrix_plus_one)
sum_matrix = np.sum(matrix)
print(f"\nСума всіх елементів масиву: {sum_matrix}")
sum_rows = np.sum(matrix, axis=1)
sum_columns = np.sum(matrix, axis=0)
print(f"\nСума по рядках: {sum_rows}")
print(f"\nСума по стовпцях: {sum_columns}")

matrix_transposed = np.transpose(matrix)
print("\nТранспонована матриця: ")
print(matrix_transposed)

min_value = np.min(matrix)
max_value = np.max(matrix)
print(f"\nМінімальне значення в матриці: {min_value}")
print(f"Максимальне значення в матриці: {max_value}")