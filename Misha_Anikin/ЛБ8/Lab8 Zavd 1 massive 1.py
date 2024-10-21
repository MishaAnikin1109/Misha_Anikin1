import array

arr = array.array('i', [1,3,7,3,9,5,10,58,20,2,105])
print("Початковий масив: ", arr)

arr.append(1009)
print("Масив після додавання елемента:", arr)
arr.remove(58)
print("Масив після видалення елемента:", arr)

print("Елемент з індексом 8: ", arr[8])

sum_arr = sum(arr)
print("Сума елементів масиву: ", sum_arr)

min_value = min(arr)
max_value = max(arr)
print(f"Мінімальне значення: {min_value}, Максимальне значення: {max_value}")

arr_sorted = array.array('i', sorted(arr))
print("Відсортованний масив: ", arr_sorted)
