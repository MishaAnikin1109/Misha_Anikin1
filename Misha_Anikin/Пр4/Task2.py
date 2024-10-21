import math

def function(x, a, b, c):
    return x**2 + math.log(abs(a)) - math.sin(b) * math.sqrt(abs(c))
x=int(input("Введіть x:"))
a=int(input("Введіть a:"))
b=int(input("Введіть b:"))
c=int(input("Введіть c:"))
print(function(x, a, b, c))