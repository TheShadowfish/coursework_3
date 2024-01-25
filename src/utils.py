import json
import os

"""
весь файл надо переработать, но думаю это проще чем с нуля собирать
"""


def get_file_path(filename):
    """
    Получает адрес папки запуска, добавляет имя файла.
    Функция необходима, чтобы программа всегда находила файлы в т.ч. при запуске её из терминала
    При запуске из IDE можно обойтись и относительными путями
    """
    # относительный путь
    filepath = os.path.join(filename)

    if not os.path.exists(filepath):
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(parent_dir, filename)
    return filepath


def load_json(filename="operations.json"):
    """
    загружает информацию файла operations.json (по умолчанию)
    filename - название файла
    data_json - возвращает json
    """
    name_path = get_file_path(filename)

    with open(name_path, "r") as read_file:
        data_json = json.load(read_file)
    return data_json


def format_skills(skills_list):
    """
    делает из list ['Python', 'Go', 'Linux'] строку Python, Go, Linux
    символы { и } тоже убирает
    """
    if skills_list == set():
        skills_list = "(пусто)"

    string_of_skills = str(skills_list).replace('[', '').replace(']', '').replace('}', '').replace('{', '').replace(
        '\'', '')
    return string_of_skills


def main():
    print(f"This is 'utils.py', need 'main.py'")


# начало программы
if __name__ == '__main__':
    main()
