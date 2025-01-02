import pytest

from maxmin import find_maxmin


def test_case_1():
    assert find_maxmin([2, 4, 1, 0, 2, -1]) == [-1, 4]


def test_case_4():
    assert find_maxmin([20, 50, 12, 6, 14, 8]) == [6, 50]


def test_case_3():
    assert find_maxmin([100, -100]) == [-100, 100]


if __name__ == '__main__':
    pytest.main()
