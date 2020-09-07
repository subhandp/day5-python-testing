
from collections import Counter 

def Mode(numbers):
    len_numbers = len(numbers) 

    data = Counter(numbers) 
    dict_data = dict(data) 
    mode = [k for k, v in dict_data.items() if v == max(list(data.values()))] 

    if len(mode) == len_numbers: 
        mode_val = None
    else: 
        mode_val =  ', '.join(map(str, mode)) 
        
    return mode_val
