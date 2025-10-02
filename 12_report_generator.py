# -*- coding: utf-8 -*-
"""Упражнение 12: Генератор отчетов о продажах"""

def _fmt_rub(n):
    return f"{n:,.0f}".replace(',', ' ') + " руб."

def report_generator():
    sales_data = [
        {"product": "Ноутбук", "price": 50000, "quantity": 3},
        {"product": "Мышь", "price": 1500, "quantity": 10},
        {"product": "Клавиатура", "price": 3000, "quantity": 5},
        {"product": "Монитор", "price": 20000, "quantity": 2}
    ]

    total_revenue = sum(item['price'] * item['quantity'] for item in sales_data)
    total_qty = sum(item['quantity'] for item in sales_data)

    # Самый продаваемый товар (по штукам)
    top_by_qty = max(sales_data, key=lambda x: x['quantity'])

    # Товар с максимальной выручкой
    top_by_revenue = max(sales_data, key=lambda x: x['price'] * x['quantity'])

    avg_ticket = total_revenue / total_qty if total_qty else 0

    print("=== ОТЧЁТ О ПРОДАЖАХ ===")
    print("Общая выручка:", _fmt_rub(total_revenue))
    print(f"Самый продаваемый товар: {top_by_qty['product']} ({top_by_qty['quantity']} шт.)")
    print(f"Товар с макс. выручкой: {top_by_revenue['product']} ({_fmt_rub(top_by_revenue['price'] * top_by_revenue['quantity'])})")
    print(f"Средний чек: {_fmt_rub(avg_ticket)}")


if __name__ == "__main__":
    report_generator()
