# -*- coding: utf-8 -*-
"""Упражнение 3: Калькулятор списков"""

def list_calculator():
    """Выполнить различные операции со списком чисел."""
    numbers = [12, 45, 23, 67, 34, 89, 56]
    print("Исходный список:", numbers)

    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    squares = [x**2 for x in numbers]
    filtered = [x for x in numbers if x > 30]
    sorted_desc = sorted(numbers, reverse=True)

    print(f"Сумма элементов: {total}")
    print(f"Среднее значение: {avg:.2f}")
    print("Квадраты чисел:", squares)
    print("Числа > 30:", filtered)
    print("Сортировка по убыванию:", sorted_desc)


if __name__ == "__main__":
    list_calculator()
