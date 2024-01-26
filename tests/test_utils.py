import json

from src import utils
import pytest


def test_utils_file_exist():
    assert utils.file_exist("operations.json").endswith("operations.json")
    assert utils.file_exist("main.py").endswith("main.py")
    assert utils.file_exist("utils.py").endswith("utils.py")


def test_utils_file_no_exist():
    with pytest.raises(FileNotFoundError):
        assert utils.file_exist("no_such_file.json")


def test_load_json():
    assert isinstance(utils.load_json("operations.json"), list)


def test_load_json_no_file():
    with pytest.raises(FileNotFoundError):
        assert utils.load_json("no_such_file.json")


def test_load_try_no_json():
    with pytest.raises(BaseException):
        assert utils.load_json("utils.py")

