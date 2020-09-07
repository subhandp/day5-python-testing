def isLeapYear(year):
    if type(year) != int:
        raise TypeError('parameter must be integer type')
    leapYear = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
    if leapYear:
        return "Kabisat"
    else:
        return "Bukan kabisat"