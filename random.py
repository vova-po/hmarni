import time


def generate_random_number():
    # Отримуємо поточний час у секундах
    current_time = time.time()

    # Використовуємо десяткову частину часу для створення випадковості
    fractional_part = current_time - int(current_time)

    # Множимо десяткову частину на 6, щоб отримати число від 0 до 6
    random_number = int(fractional_part * 6) + 1

    return random_number


def start_page():
    # Генеруємо випадкове число від 1 до 6
    random_number = generate_random_number()

    # Виводимо число
    print(f"Випадкове число від 1 до 6: {random_number}")


# Викликаємо функцію для симуляції стартової сторінки
start_page()