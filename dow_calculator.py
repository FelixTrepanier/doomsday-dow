from datetime import datetime
from util.util_functions import mod, century_leaps_adj, get_doomsday_list, get_century_start_doomsday

DATE_FORMAT = '%Y-%m-%d'
DOW_NUM = {
    0:'Sunday',
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday'
}

def dow_datetime_method(date):
    """
    Using the built in DOW calculator. Used as source of truth.
    :param date: String date in format '%Y-%m-%d'.
    :return: The day of the week of date.
    """

    dow_name = datetime.strptime(date, DATE_FORMAT).strftime('%A')
    return dow_name

def dow_doomsday_computer(date):
    """
    Using a single reference date. Can only really be done by a computer.
    :param date: String date in format '%Y-%m-%d'.
    :return: The day of the week of date.
    """

    ref_year={2000:2}
    year = int(datetime.strptime(date, DATE_FORMAT).strftime('%Y'))

    year_diff = year - list(ref_year.keys())[0]

    if year_diff < 0:
        leap_year_count = -(year_diff//-4)-1
        if year_diff%-4 == 0:
            leap_year_count = leap_year_count + 1
    elif year_diff > 0:
        leap_year_count = year_diff//4
    else:
        leap_year_count = 0

    century_leaps = century_leaps_adj(ref_year=list(ref_year.keys())[0], target_year=year)

    year_shift = leap_year_count + year_diff + century_leaps

    doomsday = datetime(year,6,6)

    day_shift = (datetime.strptime(date, DATE_FORMAT) - doomsday).days

    total_shift = mod(year_shift+day_shift, 7)
    final_dow = list(ref_year.values())[0] + total_shift

    if final_dow < 0:
        final_dow = final_dow + 7
    elif final_dow > 6:
        final_dow = final_dow - 7

    return DOW_NUM[final_dow]

def dow_doomsday_human(date):
    """
    Using the doomsdays pneumonics. Calculation can be done by humans relatively easily.
    :param date: String date in format '%Y-%m-%d'.
    :return: The day of the week of date.
    """

    year = int(datetime.strptime(date, DATE_FORMAT).strftime('%Y'))

    century_start_doomsday = get_century_start_doomsday(year)

    a = (year%100)//12
    b = (year%100)%12
    year_adjust = a + b + b//4

    doomsday_list = get_doomsday_list(year)

    if datetime.strptime(doomsday_list[0], DATE_FORMAT) > datetime.strptime(date, DATE_FORMAT):
        closest_greater_doomsday = datetime.strptime(doomsday_list[0], DATE_FORMAT)
        day_adj = (datetime.strptime(date, DATE_FORMAT) - closest_greater_doomsday).days
    else:
        doomsday_list
        closest_smaller_doomsday = datetime.strptime([i for i in doomsday_list if i < date][-1], DATE_FORMAT)
        day_adj = (datetime.strptime(date, DATE_FORMAT) - closest_smaller_doomsday).days

    final_dow = (century_start_doomsday + year_adjust + day_adj)%7

    if final_dow < 0:
        final_dow = final_dow + 7
    elif final_dow > 6:
        final_dow = final_dow - 7
    return DOW_NUM[final_dow]
