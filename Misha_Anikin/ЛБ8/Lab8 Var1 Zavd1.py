N = int(input("Введіть ціле число N: "))

divisors = [i for i in range(1, N + 1) if N % i == 0]

if len(divisors) > 2:
    divisors.remove(max(divisors))
    divisors.remove(min(divisors))
    
print("Масив після видалення найбільшого і найменшого елементів: ", divisors)