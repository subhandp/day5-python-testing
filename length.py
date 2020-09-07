def leng(text:str):
    if type(text) != str:
        raise TypeError('parameter must be string type')
    return len(text)
