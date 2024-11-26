# Исходный список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Переменная для хранения текущего индекса
index = 0

# Цикл while
while index < len(my_list):  # Условие: пока индекс не выходит за границы списка
    current_number = my_list[index]  # Получаем текущий элемент списка

    if current_number < 0:  # Проверяем, если число отрицательное
        break  # Прерываем цикл

    if current_number == 0:  # Проверяем, если число равно нулю
        index += 1  # Переходим к следующему элементу
        continue  # Пропускаем текущую итерацию

    print(current_number)  # Если число положительное, выводим его
    index += 1  # Переходим к следующему элементу
