# Нахождение суммы квадратов первых N чисел
n = int(input("Введите N: "))
sum_sq = sum(i**2 for i in range(1, n + 1))
print("Сумма квадратов:", sum_sq)
