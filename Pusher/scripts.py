import requests
import re
import csv

# this is a file made for all the funcs,
# that will not be used in production,
# but are essential for a development process


def get_best_leagues_teams_titles():

    """
    This function grabs titles of all teams in six best leagues (listed below in variable 'leagues')
    :return: list of lists each of which contains titles of all its teams
    """

    pattern_head = r'<td class="name-td alLeft bordR"><div class="hide-field"><i class="fader"></i><i class="icon-flag icon-flag_\d{4} flag-s flag-\d{4}" title="'
    pattern_tale = r'"></i><a class="name" (.*)</div>'

    leagues = [
        ['https://www.sports.ru/epl/table/', 'Англия'],
        ['https://www.sports.ru/la-liga/table/', 'Испания'],
        ['https://www.sports.ru/rfpl/table/', 'Россия'],
        ['https://www.sports.ru/seria-a/table/', 'Италия'],
        ['https://www.sports.ru/bundesliga/table/', 'Германия'],
        ['https://www.sports.ru/ligue-1/table/', 'Франция'],
    ]

    # slug_pattern = r'href="https://www.sports.ru/(.*)/"'
    title_pattern = r'title="(.*)"'

    leagues_list = []  # this list is for teams in all leagues

    # with open('teams.csv', 'w'):
    for i in range(len(leagues)):

        link, country = leagues[i]
        pattern = pattern_head + country + pattern_tale  # each league has its country name in pattern

        page = requests.get(link)
        teams = re.findall(pattern, page.text)

        teams_titles = []  # this list is for teams within one league

        for team in teams:
            # slug = re.findall(slug_pattern, team)[0]
            title = re.findall(title_pattern, team)[0]
            teams_titles.append(title)

        leagues_list.append(teams_titles)

    return leagues_list


# print(get_best_leagues_teams_titles())
