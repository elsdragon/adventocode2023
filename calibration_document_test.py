import pytest

from calibration_document import calibration_value, calibration_document, sum_calibration_document

def test_calibration_value():

    assert calibration_value('') == 0
    assert calibration_value('jljlkjsce') == 0
    assert calibration_value('1abc2') == 12
    assert calibration_value('pqr3stu8vwx') == 38
    assert calibration_value('a1b2c3d4e5f') == 15
    assert calibration_value('treb7uchet') == 77
  
    assert calibration_value('two1nine') == 29
    assert calibration_value('eightwothree') == 83
    assert calibration_value('abcone2threexyz') == 13
    assert calibration_value('xtwone3four') == 24
    assert calibration_value('4nineeightseven2') == 42 
    assert calibration_value('zoneight234') == 14
    assert calibration_value('7pqrstsixteen') ==76

def test_calibration_document():
    assert calibration_document(['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 
                                 'treb7uchet']) == [12, 38, 15, 77]
    assert calibration_document(['two1nine','eightwothree','abcone2threexyz','xtwone3four',
                                 '4nineeightseven2','zoneight234',
                                 '7pqrstsixteen']) == [29, 83, 13, 24, 42, 14, 76]
    assert calibration_document([]) == []
    assert calibration_document(['', '']) == [0, 0]


def test_sum_calibration_document():

    assert sum_calibration_document([12, 38, 15, 77]) == 142
    assert sum_calibration_document([29, 83, 13, 24, 42, 14, 76]) == 281
    assert sum_calibration_document([0,0,0]) == 0
    assert sum_calibration_document([]) == 0