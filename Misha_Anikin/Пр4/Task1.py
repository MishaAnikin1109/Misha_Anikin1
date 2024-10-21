import math

def function(x):
    return (3*math.tan(x)/math.log(math.cos(x))+4) + abs(x-x**2)
x=float(input("Введіть x:"))
print(function(x))

'''Число має бути в межах від 0 до 1'''