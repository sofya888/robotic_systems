# -*- coding: utf-8 -*-
"""Упражнение 7: Определение сезона и рекомендации по одежде"""

MONTHS = {
    'январь':1,'февраль':2,'март':3,'апрель':4,'май':5,'июнь':6,
    'июль':7,'август':8,'сентябрь':9,'октябрь':10,'ноябрь':11,'декабрь':12
}

def get_season(month: int) -> str:
    if month in (12,1,2):
        return 'зима'
    if month in (3,4,5):
        return 'весна'
    if month in (6,7,8):
        return 'лето'
    return 'осень'

def weather_advisor():
    """Дать рекомендации по одежде по сезону и температуре."""
    print("=== ПОГОДНЫЙ СОВЕТНИК ===")
    raw_month = input("Введите месяц (число 1–12 или имя по-русски): ").strip().lower()
    try:
        month = int(raw_month)
    except ValueError:
        month = MONTHS.get(raw_month, None)

    if not month or not (1 <= month <= 12):
        print("Некорректный месяц.")
        return

    try:
        t = float(input("Текущая температура (°C): ").strip().replace(',', '.'))
    except ValueError:
        print("Некорректная температура.")
        return

    season = get_season(month)
    print(f"Сейчас {season}, {t:.0f}°C") 

    # Базовые рекомендации
    if season == 'зима':
        rec = "тёплая куртка, шапка, перчатки, зимняя обувь"
    elif season == 'весна':
        rec = "лёгкая куртка/плащ, закрытая обувь"
    elif season == 'лето':
        rec = "лёгкая одежда, панама/кепка, солнцезащита"
    else:
        rec = "куртка/ветровка, непромокаемая обувь"

    # Уточнение по температуре
    if t <= -10:
        rec += "; термобельё"
    elif t <= 0:
        rec += "; шарф"
    elif t >= 28:
        rec += "; пейте больше воды"

    print("Рекомендация: " + rec)

    # Предупреждения
    if t <= -20:
        print("Осторожно! Экстремальный мороз.")
    elif t <= 0:
        print("Осторожно! Возможен гололёд.")
    if t >= 35:
        print("Предупреждение: жара. Избегайте длительного солнца.")


if __name__ == "__main__":
    weather_advisor()
