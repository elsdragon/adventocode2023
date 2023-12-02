def calibration_value(cal_val:str)->int:
    ''' 
    Select from a string first and last char that it is a number. 
    If string is empty return 0. 
    '''
    new_string: str
    digit: int

    new_string = ''
    digit = 0
    if cal_val!= '':
        new_string = ''.join(list(filter(lambda char: char in '0123456789', cal_val)))
        if new_string != '':
            digit = int(new_string[0]+new_string[-1])

    return digit


def calibration_document():
    pass


def sum_calibration_document():


    pass