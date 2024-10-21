import math

x = float(input("Введіть x:"))
y = 0.0

def funct1(x):
    return math.sin(x)

def funct2(x):
    return (math.cos(x))

def funct3(x):
    return (math.tan(x))

if x >= 3:
    y = funct1(x)  
elif 0 <= x < 3:
    y = funct2(x)
elif x < 4:
    y = funct3(x)

print("y=", y)