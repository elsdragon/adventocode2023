from file_tools import read_file
from functools import reduce

MAX_CUBE = {'red': 12, 'green': 13, 'blue': 14}

def is_dict_possible(game: dict)-> bool:
    ''' 
    Return True when set game is possible or empty set.
    False if not. 
    '''
    result = True
    for key in game:
        if (key in MAX_CUBE) and (game[key] > MAX_CUBE[key]):
            result = False
            break
    
    return result
 
    

def is_cube_possible(games: list[dict])-> bool:
    '''  
    Return True if all sets in a list are possibles, 
    False if any of then not. 
    '''
    result: bool
    result = True
    for index in range(len(games)):
        result = is_dict_possible(games[index])
        if not result:
            break
  
    return result

def lol_text(text: list[str])->list[list]:
    '''  
    Transform every string of a list in another list. 
    '''  

    new_list = []
    for index in range(len(text)):
        temp_str = text[index]
        
        new_list.append(temp_str.split(':'))
    return new_list


def transform_lol(games: list[str])-> list[dict]:
    ''' Transform list in ID and dict of games. 
    '''
    temp_dict: dict
    temp_list: list
    temp_list = []
    for element in games:
        temp_dict ={}
        key = list(filter(lambda n: n.isdigit(),element[0]))
        key = int(reduce(lambda acu, s: acu + s,key))
        value = element[1].split(';')
        value = transform_ldict(value, ',')
        index = 0
        while index < len(value):
            value[index] = transform_ldict(value[index], ' ')
            
            n_dict = {}
            for i in range(len(value[index])):
                
                k = value[index][i][2]
                v = int(value[index][i][1])
                n_dict[k] = v
            
            value[index] = n_dict

            index += 1


        temp_dict[key] = value

        temp_list.append(temp_dict)

    return temp_list

def transform_ldict(games: list[str], sp: str)->list[str]:
    new_list = []
    for index in range(len(games)):
        l = games[index].split(sp)
        new_list.append(l)
    
    return new_list

def dict_possible(games: list[dict[dict]])-> list[dict[int: bool]]:
    '''  
    
    Return a dict with key id and True or False if games are possible or not. 
    '''
    new_dict = {}
    for index in range(len(games)):
        for key, value in games[index].items():
            new_dict[key] = is_cube_possible(value)
    return new_dict

def sum_possibles(possible: dict[int:bool])-> int:
    ''' Sum key if value is True. 
    '''
    result = 0
    for key, value in possible.items():
        if value == True:
            result += key
    return result

if __name__ == '__main__':
   
    text = read_file('input2.txt')
    
    list_text = text.split('\n')
    lol_tex = lol_text(list_text)
    
    list_codes = transform_lol(lol_tex)
    #print(list_codes)
    possibles = dict_possible(list_codes)
    
    sum = sum_possibles(possibles)
    print('Sum: ', sum)