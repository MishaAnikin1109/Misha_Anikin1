import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))
List = []

x = a
y = 0

for i in range(10):
    y = (3 - math.log(abs(x - 6)) + math.cos(x))
    y = round(y, 2)
    x = round(x, 2)
    List.append(y)
    x = x + h
print(List)
print(*List, sep="\n")
    