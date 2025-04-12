def log_function_call(func):
    """Декоратор для логирования вызовов функции"""

    def wrapper(*args, **kwargs):
        # Выводим информацию о вызове функции
        print(f"Функция {func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")

        # Вызываем оригинальную функцию
        result = func(*args, **kwargs)

        # Выводим результат
        print(f"Площадь прямоугольника: {result}")
        return result

    return wrapper


@log_function_call
def calculate_area(length, width):
    """Вычисляет площадь прямоугольника"""
    return length * width


# Примеры вызова
calculate_area(5, 10)  # С позиционными аргументами
calculate_area(length=7, width=3)  # С именованными аргументами
calculate_area(4, width=6)  # Смешанный вариант