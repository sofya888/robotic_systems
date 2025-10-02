# -*- coding: utf-8 -*-
"""Упражнение 13: Шифр Цезаря (латиница и кириллица)"""

LAT_LOWER = 'abcdefghijklmnopqrstuvwxyz'
LAT_UPPER = LAT_LOWER.upper()
CYR_LOWER = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
CYR_UPPER = CYR_LOWER.upper()

def shift_char(ch, shift, mode='enc'):
    if mode == 'dec':
        shift = -shift
    if ch in LAT_LOWER:
        i = LAT_LOWER.index(ch)
        return LAT_LOWER[(i + shift) % len(LAT_LOWER)]
    if ch in LAT_UPPER:
        i = LAT_UPPER.index(ch)
        return LAT_UPPER[(i + shift) % len(LAT_UPPER)]
    if ch in CYR_LOWER:
        i = CYR_LOWER.index(ch)
        return CYR_LOWER[(i + shift) % len(CYR_LOWER)]
    if ch in CYR_UPPER:
        i = CYR_UPPER.index(ch)
        return CYR_UPPER[(i + shift) % len(CYR_UPPER)]
    return ch  # не буква — оставляем как есть

def caesar_cipher():
    print("=== ШИФР ЦЕЗАРЯ ===")
    mode = input("Выберите режим: (e) шифрование / (d) дешифрование: ").strip().lower()
    if mode not in {'e','d'}:
        print("Некорректный режим.")
        return
    try:
        shift = int(input("Сдвиг (целое число): ").strip())
    except ValueError:
        print("Сдвиг должен быть целым.")
        return
    text = input("Введите текст: \n")

    result = ''.join(shift_char(ch, shift, mode='enc' if mode=='e' else 'dec') for ch in text)
    print("Результат:")
    print(result)


if __name__ == "__main__":
    caesar_cipher()
