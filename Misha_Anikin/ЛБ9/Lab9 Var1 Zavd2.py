A = set(range(1, 26))

B = {x for x in A if x % 3 == 0}

C = {x for x in A if x % 3 != 0}

print("Множина A:", A)
print("Множина B (числа, що діляться на 3):", B)
print("Множина C (числа, що не діляться на 3):", C)