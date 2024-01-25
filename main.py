from src import utils
from src.operation import Operation


def main():
    #print(f'Здесь будут вызовы функций: чтение файла, запись экземпляров класса "операция" в массив, сортировка, вывод')
    file_name_path = utils.get_file_path("operations.json")
    json_data = utils.load_json(file_name_path)

    operations = []

    for i, item in enumerate(json_data, start=1):
        #print(f'{i}) ==> {item}')
        try:
            operations.append(Operation(item))
        except Exception as e:
            print(f"Невозможно получить операцию из данного элемента файла JSON (элемент {i}, {item}): " + str(e))

    #print('Распарсили!')
    operations2 = sorted(operations, reverse=True)

    counter_not_executed = 0;

    for i, op in enumerate(operations2, start=1):
        if op.is_executed():
            print(f'{i}) {op}')
        else:
            print(f"{i}) NOT EXECUTED!: {op}")
            counter_not_executed += 1

    print(f'TOTALLY NOT EXECUTED= {counter_not_executed} \n')
    #operations2 = sorted(operations, reverse=True)

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


# начало программы
if __name__ == '__main__':
    main()
