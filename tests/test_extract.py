from src.etl.extract import *
import pytest

URL = "https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/match-schedule-fixtures-and-results"


@pytest.fixture
def sample_page_main():
    with open('sample_data/main.html') as f:
        content = f.read()
    return content

@pytest.fixture
def sample_page_stats():
    with open('sample_data/stats.html') as f:
        content = f.read()
    return content

def test_get_page():
    page = get_page(URL)
    assert page is not None
    assert isinstance(page, bytes)

def test_scrape_links_main_page(sample_page_main):
    soup = get_soup(sample_page_main)
    cards = get_card(soup)
    list_of_links = ['https://www.espncricinfo.com' + link for link in get_each_card_href(cards)]
    for link in list_of_links:
        assert 'series/indian-premier-league-2023-1345038' in link

def test_get_batting_tables_len(sample_page_stats):
    soup = get_soup(sample_page_stats)
    assert len(get_batting_tables(soup)) == 2
     
def test_concat_all_data(sample_page_main):
    soup = get_soup(sample_page_main)
    cards = get_card(soup)
    links = ['https://www.espncricinfo.com' + link for link in get_each_card_href(cards)]
    df = concat_all_data(links)
    assert df is not None
    assert len(df) > 0
    assert all(col in df.columns for col in ["name", 'runs', 'balls_faced', 'fours', 'sixes', 'batted_out', 'date'])

