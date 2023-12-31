import pytest

from cube import is_cube_possible, is_dict_possible, sum_possibles, each_cube_need, power_of_set

def test_is_dict_possible():
    assert is_dict_possible({'blue':3, 'red': 4}) == True
    assert is_dict_possible({'green': 8, 'blue': 6, 'red': 20}) == False
    assert is_dict_possible({}) == True



def test_is_cube_possible():
    assert is_cube_possible([{'blue':3, 'red': 4}, 
                             {'red': 1, 'green': 2, 'blue': 6},
                             {'green': 2}]) == True
    
    assert is_cube_possible([{'blue': 1, 'green': 2},
                             {'green': 3, 'blue': 4, 'red': 1},
                             {'green': 1, 'blue': 1}]) == True
    
    assert is_cube_possible([{'green': 8, 'blue': 6, 'red': 20},
                             {'blue': 5, 'red': 4, 'green': 13},
                             {'green': 5, 'red': 1}]) == False
    
    assert is_cube_possible([{'green': 1, 'red': 3, 'blue': 6},
                             {'green': 3, 'red': 6},
                             {'green': 3, 'blue': 15, 'red': 14}]) == False
    
    assert is_cube_possible([{'red': 6, 'blue': 1, 'green': 3},
                             {'blue': 2, 'red': 1, 'green': 2}]) == True
    
    assert is_cube_possible([]) == True

def test_sum_possibles():
    assert sum_possibles({1: True, 2: False, 3: True, 4: False}) == 4
    assert sum_possibles({}) == 0
    assert sum_possibles({1: False, 2: False, 3: False}) == 0


def test_each_cube_need():
    assert each_cube_need([{'blue':3, 'red': 4}, 
                             {'red': 1, 'green': 2, 'blue': 6},
                             {'green': 2}]) == {'blue': 6, 'red': 4, 'green': 2}
    assert each_cube_need([{'blue': 1, 'green': 2},
                             {'green': 3, 'blue': 4, 'red': 1},
                             {'green': 1, 'blue': 1}]) == {'blue': 4, 'red': 1, 'green': 3}
    
    assert each_cube_need([{'green': 8, 'blue': 6, 'red': 20},
                             {'blue': 5, 'red': 4, 'green': 13},
                             {'green': 5, 'red': 1}]) == {'blue': 6, 'red': 20, 'green': 13}
    
    assert each_cube_need([{'green': 1, 'red': 3, 'blue': 6},
                             {'green': 3, 'red': 6},
                             {'green': 3, 'blue': 15, 'red': 14}]) == {'blue': 15, 'red': 14, 'green': 3}
    
    assert each_cube_need([{'red': 6, 'blue': 1, 'green': 3},
                             {'blue': 2, 'red': 1, 'green': 2}]) == {'blue': 2, 'red': 6, 'green': 3}

def test_power_of_set():
    assert power_of_set({'blue': 6, 'red': 4, 'green': 2}) == 48
    assert power_of_set({'blue': 4, 'red': 1, 'green': 3}) == 12
    assert power_of_set({'blue': 6, 'red': 20, 'green': 13}) == 1560
    assert power_of_set({'blue': 15, 'red': 14, 'green': 3}) == 630
    assert power_of_set({'blue': 2, 'red': 6, 'green': 3}) == 36

