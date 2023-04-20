from src.etl.extract import *
import pytest

URL = "https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/match-schedule-fixtures-and-results"


@pytest.fixture
def sample_page():
    with open('sample_data/main.html') as f:
        content = f.read()
    return content

def test_get_page():
    page = get_page(URL)
    assert page is not None
    assert isinstance(page, bytes)


def test_scrape_links_main_page(sample_page):
    soup = get_soup(sample_page)
    cards = get_card(soup)
    list_of_links = ['https://www.espncricinfo.com' + link for link in get_each_card_href(cards)]
    for link in list_of_links:
        assert 'series/indian-premier-league-2023-1345038' in link

