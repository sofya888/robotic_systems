# -*- coding: utf-8 -*-
"""Упражнение 5: Система проверки пароля"""
import string

COMMON = {
    "123456","12345678","123456789","password","qwerty","111111","123123",
    "abc123","iloveyou","admin","letmein","welcome","dragon","sunshine",
    "monkey","football","princess","000000","qwertyuiop"
}

def advanced_password_checker():
    """Усовершенствованная проверка сложности пароля (оценка 1–5)."""
    print("=== ПРОВЕРКА ПАРОЛЯ ===")
    pwd = input("Введите пароль для оценки: ")
    score = 0
    recs = []

    length_ok = len(pwd) >= 12
    upper_ok = any(c.isupper() for c in pwd)
    lower_ok = any(c.islower() for c in pwd)
    digit_ok = any(c.isdigit() for c in pwd)
    special_ok = any(c in string.punctuation for c in pwd)

    lowered = pwd.lower()
    common_hit = lowered in COMMON or any(cand in lowered for cand in ["password","qwerty","12345","admin","welcome"]) 

    score += 1 if length_ok else 0
    score += 1 if upper_ok else 0
    score += 1 if lower_ok else 0
    score += 1 if digit_ok else 0
    score += 1 if special_ok else 0

    if common_hit:
        score = max(1, score - 2)

    score = max(1, min(5, score))

    # Рекомендации
    if not length_ok:
        recs.append("увеличьте длину (≥ 12 символов)")
    if not upper_ok or not lower_ok:
        recs.append("используйте буквы обоих регистров")
    if not digit_ok:
        recs.append("добавьте цифры")
    if not special_ok:
        recs.append("добавьте спецсимволы (например, !@#$%^&*)")
    if common_hit:
        recs.append("избегайте популярных слов/последовательностей")

    print(f"Оценка безопасности: {score}/5")
    if recs:
        print("Рекомендации: " + "; ".join(recs))
    else:
        print("Отлично! Пароль выглядит надёжно (по базовым правилам).")


if __name__ == "__main__":
    advanced_password_checker()
