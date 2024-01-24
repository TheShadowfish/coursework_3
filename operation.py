from datetime import datetime


class Operation:
    """
    Поля класса:
    – дата перевода
    – описание перевода
    – откуда
    – куда
    – сумма перевода
    – валюта
    - выполнена ли операция

    Методы:
    – маскировка номера карты в формате XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
    – маскировка счета в формате **XXXX (видны только последние 4 цифры номера счета).
    - переопределить операцию сравнения (> < =): чем новее дата, тем больше экземпляр
    - возврат выполнена ли операция
    - конструктор - из элемента массива словарей
    """
    # Константа, разделяет вывод информации об операции в строке. Можно менять вывод, если надо будет (DELIMETER)
    DELIMETER = '  '

    def __init__(self, dict_operation: dict):
        """
        {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
                        }
                            },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
        },

        :param dict_operation:
        """
        self.__id: str = dict_operation['id']
        self.__state: bool = (dict_operation['state'] == 'EXECUTED')
        self.__description: str = dict_operation['description']
        self.__from: str = dict_operation.get('from')
        self.__to: str = dict_operation['to']
        self.__amount: str = dict_operation['operationAmount']['amount']
        self.__currency: str = dict_operation['operationAmount']['currency']['name']

        self.__datetime = Operation.get_datetime_from_string(dict_operation['date'])

    @staticmethod
    def get_datetime_from_string(datetime_string: str) -> datetime:
        """
        Создает объект datetime из строки
        "date": "2019-08-26T10:50:58.294041"

        Функцию strptime() можно использовать для конвертации строки в объект даты:
        """
        datetime_list = datetime_string.split('T')
        _date_str = datetime_list[0].split('-')

        _time_str = datetime_list[1].split(':')
        _sec = _time_str[2].split('.')
        # print(f'_sec {_sec}')
        # print(f'_time_str {_time_str}')
        _time_str[2] = _sec[0]
        _time_str.append(_sec[1])

        _date = [int(s) for s in _date_str]
        _time = [int(s) for s in _time_str]

        _datetime: datetime = datetime(_date[0], _date[1], _date[2], _time[0], _time[1], _time[2], _time[3])
        return _datetime

    def is_executed(self):
        """
        Выполнена ли операция
        """
        return self.__state

    @staticmethod
    def hide_card(card: str | None) -> str:
        """
        Возвращает замаскированный номер карты
        Номер карты замаскирован и не отображается целиком в формате XXXX XX ** XXXX
        (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
        Maestro 1596837868705199 -> Maestro 1596 83 5199
        Maestro 1 59683 78687 05199
        """
        if card is None:
            return ''
        else:
            card_number_hide = card[0:len(card) - 16] + card[-16:-12] + ' ' + card[-12:-10] + ' ' + card[-4:]
            return card_number_hide

    @staticmethod
    def hide_bill(bill_number: str) -> str:
        """
        Возвращает замаскированный счет
        Номер счета замаскирован и не отображается целиком в формате **XXXX
        (видны только последние 4 цифры номера счета).
        Счет 64686473678894779589 -> Счет 779589
        """
        bill_number_hide = bill_number[0:5] + bill_number[-4:]
        return bill_number_hide

    def __repr__(self):
        string_date = f'{self.__datetime.day}.{self.__datetime.month}.{self.__datetime.year}'
        string_description = f'{self.__description} {self.__from} {self.__to}'
        string_amount = f'{self.__amount} {self.__currency}'

        return (f"<Operation=(id={self.__id}, state={str(self.__state)}, string_date={string_date}, /"
                f"string_description={string_description}, /"
                f"string_amount={string_amount})>")

    def __str__(self):
        # string_date = f'{self.__datetime.day}.{self.__datetime.month}.{self.__datetime.year}'

        string_date = self.__datetime.strftime("%d.%m.%Y")

        string_from = ''
        string_to = ''
        d = Operation.DELIMETER

        if self.__from is not None and self.__from[0:4] == 'Счет':
            string_from = Operation.hide_bill(self.__from)
        else:
            string_from = Operation.hide_card(self.__from)

        if self.__to[0:4] == 'Счет':
            string_to = Operation.hide_bill(self.__to)
        else:
            string_to = Operation.hide_card(self.__to)

        string_description = f'{self.__description}{d}{string_from}{(string_from != "") * d}{string_to}'
        string_amount = f'{self.__amount} {self.__currency}'
        return f'{string_date}{d}{string_description}{d}{string_amount}'

    """
    Методы для операций сравнения:
    __lt__(self, other) — <;
    __le__(self, other) — <=;
    __eq__(self, other) — ==;
    __ne__(self, other) — !=;
    __gt__(self, other) — >;
    __ge__(self, other) — >=.
    для определения операций сравнения достаточно в классе определить только три метода: ==, <, <=, 
    если остальные являются их симметричной противоположностью. 
    В этом случае язык Python сам подберет нужный метод и выполнит его при сравнении объектов.
    """

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (datetime, Operation)):
            raise TypeError("Операнд справа должен иметь тип datetime или Operation")

        return other if isinstance(other, datetime) else other.__datetime

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.__datetime == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.__datetime < sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.__datetime <= sc

    # def __del__(self):
# class_name = self.__class__.__name__
# print('экземпляр {} уничтожен'.format(class_name))
