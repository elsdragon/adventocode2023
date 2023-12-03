
from functools import reduce

from file_tools import read_file





dict_numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 
                'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}



def calibration_value(cal_val:str)->int:
    ''' 
    Select from a string first and last char that it is a number. 
    If string is empty return 0. 
    '''
    new_string: str
    digit: int

    new_string = ''
    digit = 0
    if cal_val != '':
        for index in range(len(cal_val)):
            if cal_val[index].isdigit():
                new_string += cal_val[index]
            else:
                for num, value in dict_numbers.items():
                    if cal_val[index: index + len(num)] == num:
                        new_string += value
   
        
    if new_string != '':
        digit = int(new_string[0]+new_string[-1])

    return digit


def calibration_document(cal_doc: list[str])-> list[int]:

    '''  
    From a list of strings return a list of integer with first and last number 
    included in every string. 
    If list is empty return an empty list.
    '''
    doc_int: list[int]
    doc_int = []

    if cal_doc != []:
        doc_int = list(map(lambda element: calibration_value(element), cal_doc))

    return doc_int
    


def sum_calibration_document(doc_int: list[int])-> int:
    '''  
    Return sum of elements of a list. 
    '''
    sum = 0
    if doc_int != []:   
        sum = reduce(lambda a, b: a + b, doc_int)
    return sum


if __name__ == '__main__':
   
    text = read_file('input.txt')
    
    list_text = text.split()
    
    document = calibration_document(list_text)
    
    sum = sum_calibration_document(document)
    print('Sum: ', sum)