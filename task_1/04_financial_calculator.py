# -*- coding: utf-8 -*-
"""Упражнение 4: Финансовый калькулятор"""
import math

def _fmt_rub(n):
    return f"{n:,.2f}".replace(',', ' ').replace('.', ',') + " руб."

def financial_calculator():
    """Рассчитать сложные проценты по вкладу."""
    print("=== ФИНАНСОВЫЙ КАЛЬКУЛЯТОР ===")
    while True:
        try:
            p = float(input("Начальная сумма (руб): ").strip().replace(',', '.'))
            r = float(input("Годовая ставка (%): ").strip().replace(',', '.'))
            n = int(float(input("Срок (лет): ").strip().replace(',', '.')))
            break
        except ValueError:
            print("Ошибка ввода. Попробуйте снова.")

    target_input = input("Целевая сумма (руб), ENTER если нет: ").strip()
    target = float(target_input.replace(',', '.')) if target_input else None

    amount = p * (1 + r/100) ** n
    print(f"Через {n} лет: {_fmt_rub(amount)}")

    if target is not None:
        reached = amount >= target
        print(f"Цель {_fmt_rub(target)} достигнута: {reached}")

    if r <= 0:
        print("Ставка не положительная — сумма не удвоится.")
    else:
        years_to_double = math.log(2, 1 + r/100)
        print(f"Сумма удвоится примерно через {math.ceil(years_to_double)} лет (точно: {years_to_double:.2f})")


if __name__ == "__main__":
    financial_calculator()
