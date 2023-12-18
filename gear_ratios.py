
from file_tools import read_file
from functools import reduce

def is_valid_symbol(char: str)-> bool:
    '''Return if a char is not a digit or '.' '''
    return not char.isdigit() and char != '.'

def is_last_char(strings: list[str], index: int, position:int)-> bool:
    '''Return True if a char is the last '''
    return not position < len(strings[index]) - 1

def is_number_valid(list_strings: list[str], num: int, start_position: int, finish_position: int)-> bool:
    '''Return True if a number has a neighbour symbol valid. '''

    start_position_num = max(0, num-1)
    finish_position_num = min(num+1, len(list_strings)-1)+1
    result = False
    for i in range(start_position_num, finish_position_num):
        for j in range(start_position, finish_position):
            if is_valid_symbol(list_strings[i][j]):
                result = True
                break
    return result


def gear_ratios(list_strings: list[str])-> list[int]:

    '''find numbers with a symbol neighbour. '''

    
    new_list = []
    for i in range(len(list_strings)):
        number = ''
        start = -1
        finish = -1
        for j in range(len(list_strings[i])):
                   
            if list_strings[i][j].isdigit():
                number += list_strings[i][j]
                if start == -1:
                    start = max(0, j-1)
                else:
                    if is_last_char(list_strings, i, j):
                        finish = j +1
                        
            else:
                           
                if start != -1:
                    finish = j+1
            
            if finish != -1:
                if is_number_valid(list_strings, i, start, finish):
                    
                    new_list.append(int(number))
                number = ''
                start = -1
                finish = -1
                
    return new_list

def sum_gear_ratios(list_num: list[int])-> int:
    return reduce(lambda x, y: x +y, list_num)


if __name__ == '__main__':
   
    text = read_file('input3.txt')
    
    list_text = text.split('\n')

    num_list_valid = gear_ratios(list_text)
    suma = sum_gear_ratios(num_list_valid)
    print(suma)

