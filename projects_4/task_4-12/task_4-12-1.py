# Оптимизированная сортировка пузырьком
# Используем массив из задания: [7, 3, 8, 1, 4, 6, 2, 5]
array = [7, 3, 8, 1, 4, 6, 2, 5]
n = len(array)

for i in range(n):
    swapped = False  # Флаг: была ли перестановка?
    for j in range(0, n - i - 1):
        if array[j] > array[j + 1]:
            # Обмен элементами местами
            array[j], array[j + 1] = array[j + 1], array[j]
            swapped = True
    
    # Если перестановок не было, значит массив уже отсортирован
    if not swapped:
        break

print("Отсортированный массив:", array)
