# -*- coding: utf-8 -*-
"""Упражнение 1: Конвертер температур"""

def temperature_converter():
    """Конвертер температур между Цельсием (C), Фаренгейтом (F) и Кельвином (K)."""
    print("=== КОНВЕРТЕР ТЕМПЕРАТУР ===")
    while True:
        try:
            value = float(input("Введите значение температуры (например, 25): ").strip().replace(',', '.'))
            break
        except ValueError:
            print("Ошибка: введите число.")

    unit = input("Введите единицу измерения (C/F/K): ").strip().upper()
    if unit not in {"C","F","K"}:
        print("Ошибка: допустимы только C, F или K.")
        return

    if unit == "C":
        c = value
        f = c * 9/5 + 32
        k = c + 273.15
    elif unit == "F":
        f = value
        c = (f - 32) * 5/9
        k = c + 273.15
    else:  # K
        k = value
        c = k - 273.15
        f = c * 9/5 + 32

    # Округлим до 2 знаков
    print(f"{c:.2f}°C = {f:.2f}°F = {k:.2f}K")


if __name__ == "__main__":
    temperature_converter()
