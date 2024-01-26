import json
import os

"""
весь файл надо переработать, но думаю это проще чем с нуля собирать
"""


def file_exist(filename: str) -> str | None:
    """
    Получает адрес папки запуска, добавляет имя файла.
    Функция необходима, чтобы программа всегда находила файлы в т.ч. при запуске её из терминала
    При запуске из IDE можно обойтись и относительными путями
    """
    # относительный путь - в папке проекта
    filepath = os.path.join(filename)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл {filename} не найден в папке проекта (путь: '{filepath}')")
    else:
        return filepath


def load_json(filename="operations.json") -> list | None:
    """
    загружает информацию файла operations.json (по умолчанию)
    filename - название файла
    data_json - возвращает json
    """
    with open(filename, "r") as read_file:
        data_json = json.load(read_file)
        return data_json


