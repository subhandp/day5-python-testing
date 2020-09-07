def film_rating(rating:int):
    if type(rating) != int:
        raise TypeError('parameter must be integer type')
    if rating >= 21:
        return "DEWASA"
    elif rating >= 13:
        return "REMAJA"
    elif rating >= 9:
        return "BIMBINGAN ORANG TUA"
    else:
        return "SEMUA USIA"