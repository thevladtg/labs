#!/usr/bin/env python3
# coding=utf-8

# Программа получает ввод чисел X A B, затем выводит значение Y согласно
# y =  y = ((6 * (x ** 2)) - (a * b)) / (2 * (x ** 2)) если x > 6
# y = 4 * (x + (a ** 2) + (b ** 2)) если x <= 6


def main():  # основная функция
    # Получаем ввод X A B используя raw_input. Так как данный оператор всегда
    # возвращает тип str, преобразовываем его в int используя оператор int()
    # В питоне не обязательно объявлять переменные заранее, можно их объявлять
    # сразу же присваивая значение. Тип переменной интерпретатор определяет сам
    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x > 6:
        y = ((6 * (x ** 2)) - (a * b)) / (2 * (x ** 2))
    else:
        y = 4 * (x + (a ** 2) + (b ** 2))
    # В питоне ' и " равнозначны. Выводим результат на экран. %.1f выводит
    # значение типа float с точностью до одной десятой
    print("y = %.1f" % y)


# Следующее условие предотвращает запуск программы, если она была импортирована
# в качестве модуля (к примеру import lab1)
if __name__ == '__main__':
    main()  # вызов основной функции