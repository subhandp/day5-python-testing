def TrimWords(string:str,number:int):
    if type(string) != str:
        raise TypeError('parameter must be string type')
    
    if bool(string and string.strip()):
        raise ValueError('parameter must not empty')

    glue = ' '
    return glue.join(string.split()[0:number])
