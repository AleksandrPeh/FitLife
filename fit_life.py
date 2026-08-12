# Проект FitLife - MVP версия 1.0
daily_water_ml_per_kg = 30
ml_in_liter = 1000

print("Добрый день, давай знакомиться?")
print("-" * 30)
print("Меня зовут- дружелюбный фитнес бот 'Fitlife'")
print()

while True:
    user_name = input("Как я могу к вам обращаться?:").strip()  # имя
    if not user_name:
        print("Поле не может быть пустым, давай исправим?")
        continue
    if user_name.isdigit():
        print("Давай попробуем еще раз, только в этот раз используем буквы...")
        continue
    break

print("Мне нужно уточнить несколько ваших данных")

while True:
    user_age = int(input("Напишите ваш возраст:"))  # возраст
    if not user_age:
        print("давай попробуем еще раз?")
        continue
    else:
        print("Отлично!")
    break

while True:
    user_weight = float(input("Теперь укажем ваш вес(в кг):"))  # вес
    if not user_weight:
        print("Пример- 70")
        continue
    else:
        print("Отлично!")
    break

while True:
    user_height = float(input("рост(в метрах, например- 1.75):"))  # рост
    if not user_height:
        print("Пример- 1.75")
        continue
    else:
        print("Отлично!")
    break


bmi = user_weight / (user_height ** 2)

water_milliliters = user_weight * daily_water_ml_per_kg
water_liters = water_milliliters / ml_in_liter

print()
print()
print("=" * 50)
print(f"Выполнил отчет для вас, {user_name}!")
print(f"Ваш возраст: {user_age}")
print(f"Рекомендуемая норма воды: {water_liters:.1f} л. в день")
print(f"Ваш индекс массы тела: {bmi:.1f}")
print("=" * 40)
print("Расчет окончен. Будьте здоровы!")