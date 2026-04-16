# Нахождение факториала N!
n = int(input("Введите N: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Факториал {n}! =", fact)
