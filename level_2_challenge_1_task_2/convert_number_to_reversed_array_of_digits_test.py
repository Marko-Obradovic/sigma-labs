import pytest
from convert_number_to_reversed_array_of_digits import digitize

def test_case_1():
    assert digitize(35231) == [1, 3, 2, 5, 3]

def test_case_2():
    assert digitize(0) == [0]

def test_case_3():
    assert digitize(23582357) == [7, 5, 3, 2, 8, 5, 3, 2]

def test_case_4():
    assert digitize(984764738) == [8, 3, 7, 4, 6, 7, 4, 8, 9]

def test_case_5():
    assert digitize(45762893920) == [0, 2, 9, 3, 9, 8, 2, 6, 7, 5, 4]

def test_case_6():
    assert digitize(548702838394) == [4, 9, 3, 8, 3, 8, 2, 0, 7, 8, 4, 5]

if __name__ == '__main__':
    pytest.main()
