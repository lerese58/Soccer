import requests
import re

from settings import ALL_TAGS_PATH

# this file is made for all the funcs,
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

    title_pattern = r'title="(.*)"'

    leagues_list = []  # this list is for teams in all leagues

    for i in range(len(leagues)):

        link, country = leagues[i]
        pattern = pattern_head + country + pattern_tale  # each league has its country name in pattern

        page = requests.get(link)
        teams = re.findall(pattern, page.text)

        teams_titles = []  # this list is for teams within one league

        for team in teams:
            title = re.findall(title_pattern, team)[0]
            teams_titles.append(title)

        leagues_list.append(teams_titles)

    return leagues_list


def get_teams_tags(path=ALL_TAGS_PATH):

    """
    This function grabs tags of all teams in 'leagues' and writes them down in 'all_tags.txt'
    :return:
    """

    leagues = [
        ['https://www.sports.ru/epl/table/', 'Англия'],
        ['https://www.sports.ru/la-liga/table/', 'Испания'],
        ['https://www.sports.ru/rfpl/table/', 'Россия'],
        ['https://www.sports.ru/seria-a/table/', 'Италия'],
        ['https://www.sports.ru/bundesliga/table/', 'Германия'],
        ['https://www.sports.ru/ligue-1/table/', 'Франция'],
    ]
    
    tags = []
    pattern_head = r'<td class="name-td alLeft bordR"><div class="hide-field"><i class="fader"></i><i class="icon-flag icon-flag_\d{4} flag-s flag-\d{4}" title="'
    pattern_tale = r'"></i><a class="name" href="(.*)" title='

    club_tag_pattern = r'<h1 class="titleH1">(.*)\r\n<span class="matches-img">'
    
    for i in range(len(leagues)):

        link, country = leagues[i]
        pattern = pattern_head + country + pattern_tale

        page = requests.get(link)
        team_links = re.findall(pattern, page.text)

        print()
        print('GETTING TAGS FROM ' + country.upper())

        for team_link in team_links:
            team_page = requests.get(team_link)

            tag = re.search(club_tag_pattern, team_page.text)
            if tag:
                tag = tag.group(1).lower()
                print(tag)
                tags.append(tag)

    tags = sorted(tags)
    with open(path, 'w') as file:
        for tag in tags:
            file.write(tag + '\n')
