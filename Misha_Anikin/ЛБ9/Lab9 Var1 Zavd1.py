def string_to_tuple(input_string):
    numbers_list = input_string.split()
    numbers_tuple = tuple(float(number) for number in numbers_list)
    return numbers_tuple

input_string = input("Введіть рядок з дійсними числами, розділеними пробілами: ")

result_tuple = string_to_tuple(input_string)

print("Отриманий кортеж:", result_tuple)