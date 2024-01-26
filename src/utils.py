import json
import os



def file_exist(filename: str) -> str | None:
    """
    Получает адрес папки запуска, добавляет имя файла.
    Ищет файл в папке из которой запустили скрипт, затем в папке, где он лежит, затем в родительской директории
    Функция необходима, чтобы программа всегда находила файлы в т.ч. при запуске её из терминала
    При запуске из IDE можно обойтись и относительными путями
    """
    # относительный путь - в папке проекта
    filepath = os.path.join(filename)
    # print(f"filepath {filepath}")
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # print(f"parent_dir {parent_dir}")
    base_dir = os.path.dirname(parent_dir)
    # print(f"base_dir {base_dir}")

    # if os.path.exists(filepath):
    #     return filepath
    if os.path.exists(os.path.join(parent_dir, filename)):
        return os.path.join(parent_dir, filename)
    elif os.path.exists(os.path.join(base_dir, filename)):
        return os.path.join(base_dir, filename)
    else:
        raise FileNotFoundError(f"Файл {filename} не найден (пути поиска: '{base_dir}, {base_dir}')")
        return None


def load_json(filename="operations.json") -> list | None:
    """
    загружает информацию файла operations.json (по умолчанию)
    filename - название файла
    data_json - возвращает json
    """
    with open(filename, "r") as read_file:
        data_json = json.load(read_file)
        return data_json


