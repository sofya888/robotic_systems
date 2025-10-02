# -*- coding: utf-8 -*-
"""Упражнение 14: Симулятор банкомата"""

def atm_simulator():
    balance = 10000  # начальный баланс
    CASH_LIMIT = 5000  # лимит на снятие за одну операцию
    print("=== БАНКОМАТ ===")
    while True:
        print(f"\nТекущий баланс: {balance} руб.")
        print("1. Показать баланс")
        print("2. Снять наличные")
        print("3. Пополнить счёт")
        print("4. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            print(f"Баланс: {balance} руб.")
        elif choice == '2':
            try:
                amt = int(float(input("Сумма снятия (кратно 100): ").strip()))
            except ValueError:
                print("Некорректная сумма.")
                continue
            if amt <= 0:
                print("Сумма должна быть положительной.")
            elif amt % 100 != 0:
                print("Сумма должна быть кратна 100.")
            elif amt > CASH_LIMIT:
                print(f"Превышен лимит одной операции: {CASH_LIMIT} руб.")
            elif amt > balance:
                print("Недостаточно средств.")
            else:
                balance -= amt
                print(f"Выдано: {amt} руб. Новый баланс: {balance} руб.")
        elif choice == '3':
            try:
                amt = int(float(input("Сумма пополнения (кратно 100): ").strip()))
            except ValueError:
                print("Некорректная сумма.")
                continue
            if amt <= 0:
                print("Сумма должна быть положительной.")
            elif amt % 100 != 0:
                print("Сумма должна быть кратна 100.")
            else:
                balance += amt
                print(f"Зачислено: {amt} руб. Новый баланс: {balance} руб.")
        elif choice == '4':
            print("Спасибо! До свидания.")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    atm_simulator()
