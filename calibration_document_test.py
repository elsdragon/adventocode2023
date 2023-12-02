import pytest

from calibration_document import calibration_value, calibration_document, sum_calibration_document

def test_calibration_value():

    assert calibration_value('') == 0
    assert calibration_value('jljlkjsce') == 0
    assert calibration_value('1abc2') == 12
    assert calibration_value('pqr3stu8vwx') == 38
    assert calibration_value('a1b2c3d4e5f') == 15
    assert calibration_value('treb7uchet') == 77

def test_calibration_document():
    assert calibration_document(['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']) == [12, 38, 15, 77]
    assert calibration_document([]) == []
    assert calibration_document(['', '']) == [0, 0]


def test_sum_calibration_document():

    assert sum_calibration_document([12, 38, 15, 77]) == 142
    assert sum_calibration_document([0,0,0]) == 0
    assert sum_calibration_document([]) == 0