from src.operation import Operation
import pytest


def test_operation__init__(one_dict_fixture):
    assert isinstance(Operation(one_dict_fixture), Operation)
# @pytest.mark.parametrize('array, type_in_array, expected', [
#     ([1, 2, 3], int, 3),
#    ([1, '2', '3'], str, 2),
#    (['1', 2, '3'], int, 1) ])