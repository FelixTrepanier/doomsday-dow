def mod(n, base):
    """
    "absolute" modulo
    :param n: n%base
    :param base: n%base
    :return: Int
    """
    if n < 0:
        shift = (n)%-base
    elif n > 0:
        shift = (n)%base
    else:
        shift = 0
    return shift

def century_leaps_adj(ref_year, target_year):
    """
    Accounting for leap years not happening on years divisible by 100 but not 400.
    :param ref_year: Reference year.
    :param target_year: Target year.
    :return: int
    """
    if ref_year > target_year:
        century_list = [i for i in range(target_year+1,ref_year+1) if i%100==0 and i%400!=0]
        adj = len(century_list)
    elif ref_year < target_year:
        century_list = [i for i in range(ref_year,target_year+1) if i%100==0 and i%400!=0]
        adj = -len(century_list)
    else:
        adj = 0
    return adj

def get_doomsday_list(year):
    doomsdays = [
        '04-04',
        '06-06',
        '08-08',
        '10-10',
        '12-12',
        '07-11',
        '11-07',
        '05-09',
        '09-05'
    ]
    leap_year_doomsdays = [
        '01-04',
        '02-29'
    ]
    non_leap_year_doomsdays = [
        '01-03',
        '02-28'
    ]
    if year%4!=0 or (year%100==0 and year%400!=0):
        all_doomsdays = non_leap_year_doomsdays + doomsdays
    else:
        all_doomsdays = leap_year_doomsdays + doomsdays
    l = []

    string_year = str(year)
    while len(string_year)<4:
        string_year = f'0{string_year}'

    for i in sorted(all_doomsdays):
        l = l + [f'{string_year}-{i}']

    return l

def get_century_start_doomsday(year):
    """
    Get the doomsday DOW for the first year of a century.
    :param year: Year from which to get the century.
    :return: The doomsday DOW number for the first year of a century.
    """
    century_dow_seq = {
        0:2,
        1:6,
        2:5,
        3:3
    }

    return century_dow_seq[(year//100)%4]