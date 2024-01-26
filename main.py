from src import utils
from src.operation import Operation


def main():
    FILENAME = "operations.json"

    file_name_path = utils.file_exist(FILENAME)
    if file_name_path is None:
        print(f"Файл {FILENAME} не найден по указанному пути")
        exit(1)
    json_data = utils.load_json(FILENAME)

    operations = []

    for i, item in enumerate(json_data, start=1):
        #print(f'{i}) ==> {item}')
        try:
            operations.append(Operation(item))
        except Exception as e:
            print(f"Невозможно получить операцию из данного элемента файла JSON (элемент {i}, {item}): " + str(e))

    operations2 = sorted(operations, reverse=True)

    counter_not_executed = 0;

    for i, op in enumerate(operations, start=1):
        if op.is_executed():
            print(f'{i}) {op}')
        else:
            print(f"{i}) NOT EXECUTED!: {op}")
            counter_not_executed += 1
    print(f' NOT EXECUTED = {counter_not_executed} \n')

    # Список из 5 последних операций вывести
    latest_operations = 5
    counter = latest_operations

    for op in operations2:
        if op.is_executed():
            print(op)
            counter -= 1
        if counter < 1:
            print(f"Последние {latest_operations} успешных операций выведены")
            break
    # num = None
    try:
        file_name_path = 'main.py'
        json_data = utils.load_json(file_name_path)
        print(f"<type> {type(json_data)}")
    except Exception as e:
        print("Файл точно не является JSON " + str(e))

# начало программы
if __name__ == '__main__':
    main()
