import json

from src import utils
import pytest


def test_utils_file_exist():
    assert utils.file_exist("operations.json") == "operations.json"
    assert utils.file_exist("main.py") == "main.py"


def test_load_json_no_file():
    with pytest.raises(FileNotFoundError):
        assert utils.load_json("no_such_file.json")


def test_load_try_no_json():
    with pytest.raises(BaseException):
        assert utils.load_json("operation.py")

