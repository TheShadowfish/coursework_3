from src import utils
from src.operation import Operation


def main():
    FILENAME = "operations.json"
    latest_operations = 5
    error_list: list[str] = []
    operations = []

    file_name_path = utils.file_exist(FILENAME)
    if file_name_path is None:
        print(f"Файл {FILENAME} не найден")
        exit(1)
    json_data = utils.load_json(file_name_path)

    for i, item in enumerate(json_data, start=1):
        try:
            operations.append(Operation(item))
        except Exception as e:
            error_list.append(f'{file_name_path}, элемент {i}, {item}): {str(e)}')

    operations2 = sorted(operations, reverse=True)
    counter = latest_operations

    print(f"Последние {latest_operations} успешных операций клиента: \n")

    for op in operations2:
        if op.is_executed():
            print(op)
            counter -= 1
        if counter < 1:
            break


# начало программы
if __name__ == '__main__':
    main()
