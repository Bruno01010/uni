import os  # Импортируем модуль os для работы с файловой системой
import time  # Импортируем модуль time для работы с временем

# Указываем директорию для обхода (текущая директория)
directory = "."

# Обходим директорию с помощью os.walk
for root, dirs, files in os.walk(directory):
    for file in files:  # Перебираем все файлы в текущем каталоге
        filepath = os.path.join(root, file)  # Формируем полный путь к файлу
        filetime = os.path.getmtime(filepath)  # Получаем время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Форматируем время
        filesize = os.path.getsize(filepath)  # Получаем размер файла в байтах
        parent_dir = os.path.dirname(filepath)  # Получаем родительскую директорию файла

        # Выводим информацию о файле
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')