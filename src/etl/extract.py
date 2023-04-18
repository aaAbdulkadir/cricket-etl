from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


from time import sleep

WEBDRIVER_PATH = "webdriver/chromedriver.exe"
CHROME_PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"
URL = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-schedule-fixtures-and-results"
# "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
# https://hub.docker.com/r/selenium/standalone-chrome dockerizing selenium
# currently running on windows because of selenium

def get_driver(chrome_path, webdriver_path):
    chrome_options = Options()
    chrome_options.binary_location = chrome_path
    service = Service(executable_path=webdriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def get_website(driver, url):
    driver.get(url)

def tear_down(driver):
    driver.close()

def handle_popup():
    pass

driver = get_driver(CHROME_PATH, WEBDRIVER_PATH)
get_website(driver, URL)


sleep(100)
tear_down(driver)





