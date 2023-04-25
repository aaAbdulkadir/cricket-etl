from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

URL = "https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/match-schedule-fixtures-and-results"

def get_page(url):
    return requests.get(url).content

def get_soup(page):
    return BeautifulSoup(page, 'lxml')

def get_card(soup):
    return soup.find_all(class_=re.compile('ds-p-4 hover:ds-bg-ui-fill-translucent'))

def get_each_card_href(cards):
    return [card.find('a') ['href'] for card in cards]

def scrape_links_main_page():
    web = get_page(URL)
    soup = get_soup(web)
    cards = get_card(soup)
    return  ['https://www.espncricinfo.com' + link for link in get_each_card_href(cards)]

def get_date(soup):
    return (soup.find(class_='ds-text-tight-m ds-font-regular ds-text-typo-mid3').text.strip()).split(',')[2]

# def get_teams(soup):
#     teams = soup.find_all(class_='ds-text-title-xs ds-font-bold ds-capitalize')
#     return [team.text.strip() for team in teams]

def get_batting_tables(soup):
    return soup.find_all('table', class_=re.compile('ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table'))

def get_batting_stats(table, date):
    batters = []
    tr_tags = table.find_all('tr')
    for tr in tr_tags:
        td_tags = tr.find_all('td')
        try:
            player_name = td_tags[0].text.strip()
            runs = td_tags[2].text.strip()
            balls = td_tags[3].text.strip()
            fours = td_tags[5].text.strip()
            sixes = td_tags[6].text.strip()
            batted_out = td_tags[1].text.strip()

            batter_stats = {
                "name": player_name,
                "runs": runs,
                "balls_faced": balls,
                "fours": fours,
                "sixes": sixes,
                "batted_out": batted_out,
                "date": date
            }
            batters.append(batter_stats)
        except:
            pass   
    return batters

def scrape_data_link(link):
    web = get_page(link)
    soup = get_soup(web)
    date = get_date(soup)
    tables = get_batting_tables(soup)
    len_tables = len(tables)

    if len_tables > 0:
        batters = [get_batting_stats(table, date) for table in tables]
        print(f'Data collected for {date}')
        return batters
    else:
        print(f'{date} has no data')
        return None

def concat_all_data(links):
    df_list = []
    for link in links:
        data = scrape_data_link(link)
        if data:
            for table in data:
                df_list.append(pd.DataFrame(table))
    if not df_list:
        return None
    return pd.concat(df_list, ignore_index=True)

def extract():
    links = scrape_links_main_page() # get links
    table = concat_all_data(links) # get final df
    table.to_csv('data/scraped_data.csv') # save df
    print('Data extracted.')
    return table

"""RUN SCRIPT"""
extract()