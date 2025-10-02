# -*- coding: utf-8 -*-
"""Упражнение 11: Система управления студентами"""

def format_table(rows, headers):
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    line = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    def fmt_row(vals):
        return "| " + " | ".join(str(v).ljust(w) for v, w in zip(vals, widths)) + " |"
    parts = [line, fmt_row(headers), line]
    for r in rows:
        parts.append(fmt_row(r))
    parts.append(line)
    return "\n".join(parts)

def student_management_system():
    students = []  # каждый студент: dict(name:str, age:int, grades:list[int])
    while True:
        print("\n=== СИСТЕМА УПРАВЛЕНИЯ СТУДЕНТАМИ ===")
        print("1. Добавить студента")
        print("2. Показать всех студентов")
        print("3. Найти студента по имени")
        print("4. Рассчитать средний балл по группе")
        print("5. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            name = input("Имя: ").strip()
            try:
                age = int(input("Возраст: ").strip())
            except ValueError:
                print("Возраст должен быть числом.")
                continue
            grades_raw = input("Оценки через запятую (например: 5,4,3): ").strip()
            try:
                grades = [int(x) for x in grades_raw.replace(' ', '').split(',') if x]
            except ValueError:
                print("Оценки должны быть целыми числами.")
                continue
            students.append({"name": name, "age": age, "grades": grades})
            print("Студент добавлен.")

        elif choice == "2":
            if not students:
                print("Нет студентов.")
                continue
            rows = []
            for s in students:
                avg = sum(s['grades'])/len(s['grades']) if s['grades'] else 0
                rows.append([s['name'], s['age'], ", ".join(map(str, s['grades'])), f"{avg:.2f}"])
            print(format_table(rows, headers=["Имя","Возраст","Оценки","Средний балл"]))

        elif choice == "3":
            query = input("Введите имя или часть имени: ").strip().lower()
            found = [s for s in students if query in s['name'].lower()]
            if not found:
                print("Ничего не найдено.")
            else:
                rows = []
                for s in found:
                    avg = sum(s['grades'])/len(s['grades']) if s['grades'] else 0
                    rows.append([s['name'], s['age'], ", ".join(map(str, s['grades'])), f"{avg:.2f}"])
                print(format_table(rows, headers=["Имя","Возраст","Оценки","Средний балл"]))

        elif choice == "4":
            if not students:
                print("Нет студентов.")
                continue
            all_grades = [g for s in students for g in s['grades']]
            group_avg = sum(all_grades)/len(all_grades) if all_grades else 0
            print(f"Средний балл по группе: {group_avg:.2f}")

        elif choice == "5":
            print("Выход.")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    student_management_system()
