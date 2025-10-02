# -*- coding: utf-8 -*-
"""Упражнение 6: Калькулятор налога"""

def tax_for_income(income: float) -> float:
    # Прогрессивная шкала:
    # до 15_000: 0%
    # 15_001–50_000: 15%
    # 50_001–100_000: 25%
    # свыше 100_000: 30%
    tax = 0.0
    if income <= 15000:
        return 0.0

    # часть 15_001–50_000
    part = min(income, 50000) - 15000
    if part > 0:
        tax += part * 0.15

    # часть 50_001–100_000
    if income > 50000:
        part = min(income, 100000) - 50000
        tax += part * 0.25

    # часть свыше 100_000
    if income > 100000:
        part = income - 100000
        tax += part * 0.30

    return tax

def tax_calculator():
    """Рассчитать налог и чистый доход."""
    print("=== КАЛЬКУЛЯТОР НАЛОГА ===")
    try:
        income = float(input("Годовой доход (руб): ").strip().replace(',', '.'))
    except ValueError:
        print("Ошибка ввода.")
        return

    tax = tax_for_income(income)
    net = income - tax
    print(f"Налог: {tax:,.2f} руб.".replace(',', ' ').replace('.', ','))
    print(f"Чистый доход: {net:,.2f} руб.".replace(',', ' ').replace('.', ','))


if __name__ == "__main__":
    tax_calculator()
