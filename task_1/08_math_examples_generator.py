# -*- coding: utf-8 -*-
"""Упражнение 8: Генератор математических примеров"""
import random
import operator

def math_examples_generator():
    """Сгенерировать 10 случайных примеров, спросить ответы и оценить результат."""
    print("=== МАТ. ПРИМЕРЫ ===")
    ops = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
        ('/', operator.floordiv),  # деление с целым результатом
    ]
    total = 10
    correct = 0

    for i in range(1, total + 1):
        op_symbol, op_func = random.choice(ops)
        if op_symbol == '/':
            b = random.randint(2, 12)
            a = b * random.randint(1, 12)  # гарантирует целый результат
        elif op_symbol == '*':
            a = random.randint(2, 12)
            b = random.randint(2, 12)
        else:
            a = random.randint(5, 50)
            b = random.randint(1, 50)

        right = op_func(a, b)
        try:
            ans_raw = input(f"{i}. {a} {op_symbol} {b} = ? Ответ: ").strip()
            ans = int(ans_raw)
        except ValueError:
            ans = None

        if ans == right:
            correct += 1
            mark = "✅"
        else:
            mark = f"❌ (правильно: {right})"
        print(mark)

    pct = (correct / total) * 100
    print(f"Результат: {correct}/{total} правильных ответов ({pct:.0f}%)")


if __name__ == "__main__":
    math_examples_generator()
