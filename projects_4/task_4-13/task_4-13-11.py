# Среднее арифметическое элементов с четными индексами
arr = [10, 20, 30, 40, 50, 60]
even_idx_elements = [arr[i] for i in range(len(arr)) if i % 2 == 0]
avg_even = sum(even_idx_elements) / len(even_idx_elements)
print("Среднее арифметическое (четные индексы):", avg_even)
