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
    return  ['https://www.espncricinfo.com/' + link for link in get_each_card_href(cards)]

def get_stats_table(soup):
    return len(soup.find_all('table', class_=re.compile('ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table')))



def get_table_rows(table):
    td_tags = table.find_all('td', )

    
def scrape_info_each_link(links):
    for link in links:
        try:
            print(link)
            web = get_page(link)
            soup = get_soup(web)
            print(get_stats_table(soup))
        except:
            print('date note here')

"""RUN SCRIPT"""
links = scrape_links_main_page()
table = scrape_info_each_link(links)



