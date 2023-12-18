import pytest

from gear_ratios import gear_ratios, sum_gear_ratios



def test_gear_ratios():
    assert gear_ratios(['467..114..', 
                       '...*......',
                       '..35..633.',
                       '......#...',
                       '617*......',
                       '.....+.58.',
                       '..592.....',
                       '......755.',
                       '...$.*....',
                       '.664.598..']) == [467, 35, 633, 617, 592, 755, 664, 598]
    
def test_sum_gear_ratios():
    assert sum_gear_ratios([467, 35, 633, 617, 592, 755, 664, 598]) == 4361