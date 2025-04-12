def append_to_file(text, filename):
    # Открываем файл в режиме добавления
    with open(filename, 'a') as file:
        file.write(text + '\n')  # Записываем текст с новой строки

    # Читаем содержимое файла с помощью контекстного менеджера
    with open(filename, 'r') as file:
        lines = file.readlines()  # Получаем все строки файла

    # Выводим четные строки (индексация с нуля, поэтому четные индексы - 1, 3, 5 и т.д.)
    even_lines = [line.strip() for index, line in enumerate(lines) if index % 2 != 0]  # Индексы 1, 3, 5, ...
    for line in even_lines:
        print(line)

# Пример использования функции
append_to_file("gaga", "example.txt")
