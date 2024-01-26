from src import utils
from src.operation import Operation


def main():
    FILENAME = "operations.json"
    latest_operations = 5
    error_list: list[str] = []

    file_name_path = utils.file_exist(FILENAME)
    if file_name_path is None:
        print(f"Файл {FILENAME} не найден")
        # error_list.append(f"Файл {FILENAME} не найден в папке программы")
        exit(1)

    json_data = utils.load_json(file_name_path)

    operations = []

    for i, item in enumerate(json_data, start=1):
        # print(f'{i}) ==> {item}')
        try:
            operations.append(Operation(item))
        except Exception as e:
            error_list.append(f'{file_name_path}, элемент {i}, {item}): {str(e)}')
            # print(f"Невозможно получить операцию из данного элемента файла JSON ({file_name_path}, элемент {i}, {item}): " + str(e))

    operations2 = sorted(operations, reverse=True)

    # counter_not_executed = 0;
    # for i, op in enumerate(operations, start=1):
    #     if op.is_executed():
    #         print(f'{i}) {op}')
    #     else:
    #         print(f"{i}) NOT EXECUTED!: {op}")
    #         counter_not_executed += 1
    # print(f' NOT EXECUTED = {counter_not_executed} \n')

    # Список из 5 последних операций вывести

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
