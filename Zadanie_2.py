import math

def prime_numbers():
    """Генератор простых чисел"""
    num = 2  # первое простое число
    while True:
        is_prime = True
        # Проверяем делители от 2 до квадратного корня числа
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

# Пример использования генератора
primes = prime_numbers()
for _ in range(10):  # получаем первые 10 простых чисел
    print(next(primes))