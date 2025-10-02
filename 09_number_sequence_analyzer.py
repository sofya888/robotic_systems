# -*- coding: utf-8 -*-
"""Упражнение 9: Анализ последовательности чисел"""
import statistics

BLOCKS = "▁▂▃▄▅▆▇█"  # 8 уровней

def sparkline(nums):
    if not nums:
        return ""
    mn, mx = min(nums), max(nums)
    if mx == mn:
        return BLOCKS[-1] * len(nums)
    res = []
    for x in nums:
        # нормируем в [0..7]
        idx = int((x - mn) / (mx - mn) * (len(BLOCKS)-1))
        res.append(BLOCKS[idx])
    return "".join(res)

def number_sequence_analyzer():
    """Считать числа до 'stop' и вывести статистику и график."""
    print("=== АНАЛИЗ ПОСЛЕДОВАТЕЛЬНОСТИ ===")
    nums = []
    while True:
        s = input("Введите число или 'stop' для завершения: ").strip().lower()
        if s == 'stop':
            break
        try:
            x = float(s.replace(',', '.'))
            nums.append(x)
        except ValueError:
            print("Не число. Повторите.")

    count = len(nums)
    if count == 0:
        print("Нет данных.")
        return

    mx, mn = max(nums), min(nums)
    avg = sum(nums)/count
    has_dups = len(set(nums)) < len(nums)

    nums_sorted = sorted(nums)
    median = statistics.median(nums_sorted)

    print(f"Чисел введено: {count}")
    print(f"Максимум: {mx}, Минимум: {mn}, Среднее: {avg:.2f}")
    print(f"Медиана: {median}")
    print("Повторяющиеся значения:", "есть" if has_dups else "нет")
    print("График:", sparkline(nums))


if __name__ == "__main__":
    number_sequence_analyzer()
