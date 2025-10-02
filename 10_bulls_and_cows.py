# -*- coding: utf-8 -*-
"""Упражнение 10: Игра 'Быки и коровы'"""
import random

def secret_number():
    digits = list('0123456789')
    first = random.choice(digits[1:])  # первая цифра не ноль
    digits.remove(first)
    number = [first]
    while len(number) < 4:
        d = random.choice(digits)
        digits.remove(d)
        number.append(d)
    return ''.join(number)

def bulls_and_cows():
    print("=== БЫКИ И КОРОВЫ ===")
    secret = secret_number()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = input(f"Попытка {attempt}/{attempts}. Введите 4-значное число: ").strip()
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4 or guess[0] == '0':
            print("Некорректный ввод. Число должно быть из 4 уникальных цифр и не начинаться с 0.")
            continue

        bulls = sum(1 for i in range(4) if guess[i] == secret[i])
        cows = sum(1 for ch in guess if ch in secret) - bulls
        print(f"Быки: {bulls}, Коровы: {cows}")

        if bulls == 4:
            print(f"Поздравляем! Вы угадали число {secret} за {attempt} попыток!")
            return

    print(f"Увы! Вы не угадали. Число было: {secret}")


if __name__ == "__main__":
    bulls_and_cows()
