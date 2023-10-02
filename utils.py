from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError
from datetime import datetime


def data_processing(dict_info: dict) -> dict:
    titles = int(dict_info["titles"])

    if titles < 0:
        raise NegativeTitlesError()

    start_of_the_cups = 1930
    current_year = datetime.now().year
    first_cup_date = dict_info["first_cup"]
    first_cup_year = datetime.strptime(first_cup_date, "%Y-%m-%d").year

    cup_exists = 0
    cups_counter = 0

    for x_year in range(start_of_the_cups, current_year, 4):
        if x_year == first_cup_year:
            cup_exists = x_year

        if x_year >= first_cup_year:
            cups_counter = cups_counter + 1

    if cup_exists == 0:
        raise InvalidYearCupError()

    if titles > cups_counter:
        raise ImpossibleTitlesError()

    return dict_info
