# -*- coding: utf-8 -*-
"""Упражнение 2: Анализатор текста"""
import re

def text_analyzer():
    """Проанализировать введенный текст и вывести статистику."""
    print("=== АНАЛИЗАТОР ТЕКСТА ===")
    text = input("Введите текст: \n")

    # Символы
    chars = len(text)

    # Слова (включая кириллицу и латиницу, цифры и дефисы)
    words = re.findall(r"[A-Za-zА-Яа-яЁё0-9-]+", text, flags=re.UNICODE)
    words_count = len(words)

    # Предложения (по . ! ?)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    sentences_count = len(sentences)

    # Самое длинное слово
    longest = max(words, key=len) if words else ""

    # Проценты заглавных/строчных букв среди буквенных символов
    letters = [c for c in text if c.isalpha()]
    upper = sum(1 for c in letters if c.isupper())
    lower = sum(1 for c in letters if c.islower())
    total_letters = len(letters)
    upper_pct = (upper / total_letters * 100) if total_letters else 0.0
    lower_pct = (lower / total_letters * 100) if total_letters else 0.0

    # Количество цифр
    digits = sum(1 for c in text if c.isdigit())

    print(f"Символов: {chars}, Слов: {words_count}, Предложений: {sentences_count}")
    if longest:
        print(f"Самое длинное слово: '{longest}' ({len(longest)} символов)")
    print(f"Буквы: заглавных {upper_pct:.1f}%, строчных {lower_pct:.1f}%")
    print(f"Цифр в тексте: {digits}")


if __name__ == "__main__":
    text_analyzer()
