# Вычисление суммы первых N натуральных чисел
n = int(input("Введите N: "))
total_sum = sum(range(1, n + 1))
print(f"Сумма первых {n} чисел:", total_sum)
