import random

# создаем массив со случайными целыми числами
array = [[random.randint(1, 99) for _ in range(5)] for _ in range(4)]

# находим максимальное число в массиве
max_value = max(max(row) for row in array)

# находим индекс строки, содержащей максимальное число
max_row_index = 0
for i, row in enumerate(array):
    if max_value in row:
        max_row_index = i
        break

# находим индекс столбца, содержащего максимальное число
max_column_index = array[max_row_index].index(max_value)

# выводим индекс и значение максимального числа на экран
print(f"Индекс максимального числа: ({max_row_index}, {max_column_index})")
print(f"Значение максимального числа: {max_value}")
print("Массив:")
for row in array:
    print(row)

even_elements_count = 0
for i in range(max_row_index):
    for j in range(max_column_index):
        if array[i][j] % 2 == 0:
            even_elements_count += 1
print(f"Количество четных целых элементов перед максимальным числом: {even_elements_count}")

new_value = even_elements_count + max_value
array[max_row_index][max_column_index] = new_value
print("Массив:")
for row in array:
    print(row)