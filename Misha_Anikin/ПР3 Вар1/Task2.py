import math
import sys

num=int(input("Введіть трицифрове число: "))

num=int(num)
digits=[int(digit) for digit in str(num)]
result=(digits[0]+digits[1]+digits[2])//3
print(result)