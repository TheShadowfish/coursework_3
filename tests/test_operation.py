from src.operation import Operation
import pytest


def test_operation__init__(one_right_dict_fixture):
    assert isinstance(Operation(one_right_dict_fixture), Operation)


def test_operation__init__wrong_datetime(one_dict_wrong_data_fixture):
    with pytest.raises(ValueError):
        assert Operation(one_dict_wrong_data_fixture)


def test_operation__init__incorrect_data():
    with pytest.raises(ValueError):
        assert Operation({})


def test_operation__init__from_is_empty(one_dict_no_from_fixture):
    assert isinstance(Operation(one_dict_no_from_fixture), Operation)


def test_operation_datetime_from_string():
    assert Operation.get_datetime_from_string("2019-08-26T10:50:58.294041")


def test_operation_datetime_from_string_error():
    with pytest.raises(ValueError):
        assert Operation.get_datetime_from_string("2019/08/26 10-50:58.294041")


def test_operation_is_executed(one_right_dict_fixture, dict_cancelled_fixture):
    assert Operation(one_right_dict_fixture).is_executed() is True
    assert Operation(dict_cancelled_fixture).is_executed() is False


@pytest.mark.parametrize('string_or_none, expected', [
    (None, ''),
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 3152479541115065', 'MasterCard 3152 47** **** 5065'),
    ('Visa Gold 9447344650495960', 'Visa Gold 9447 34** **** 5960')
])
def test_operation_hide_info(string_or_none, expected):
    assert Operation.hide_info(string_or_none) == expected


def test_operation_hide_info_error():
    with pytest.raises(ValueError):
        assert Operation.hide_info('Phone Numer 89817654321')


def test_operation__str__(dict_list_fixture, dict_list_str_fixture):
    for i in range(0, 5):
        assert Operation(dict_list_fixture[i]).__str__() == dict_list_str_fixture[i]



@pytest.fixture
def operations(one_right_dict_fixture, one_dict_no_from_fixture):
    # op1 2019-08-26T10:50:58.294041
    # op2 2018-03-23T10:45:06.972075
    # op3 = op2
    op1 = Operation(one_right_dict_fixture)
    op2 = Operation(one_dict_no_from_fixture)
    op3 = Operation(one_right_dict_fixture)
    op1_time = Operation.get_datetime_from_string(one_right_dict_fixture['date'])
    return [op1, op2, op3, op1_time]


def test_operation__eq__(operations):
    assert (operations[0].__eq__(operations[1])) is False
    assert (operations[0].__eq__(operations[2])) is True
    assert (operations[0].__eq__(operations[3])) is True
    assert (operations[1].__eq__(operations[3])) is False


def test_operation__lt__(operations):
    # __lt__(self, other) — <;
    assert (operations[0].__lt__(operations[1])) is False
    assert (operations[0].__lt__(operations[2])) is False
    assert (operations[1].__lt__(operations[3])) is True
    assert (operations[1].__lt__(operations[0])) is True


def test_operation__le__(operations):
    # __le__(self, other) — <=;
    assert (operations[0].__le__(operations[1])) is False
    assert (operations[0].__le__(operations[2])) is True
    assert (operations[1].__le__(operations[3])) is True
    assert (operations[2].__le__(operations[3])) is True


def test_operation__verify_data(one_right_dict_fixture):
    op1 = Operation(one_right_dict_fixture)
    with pytest.raises(TypeError):
        op1.__eq__('no_operation_no_datetime')

