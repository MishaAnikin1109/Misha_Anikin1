import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

x = a

while x <= b:
    y = 3 - math.log(abs(x - 6)) + math.cos(x)
    y = round(y, 2)
    x = round(x, 2)
    print(x, " ", y)
    x = x + h