import json
import socket, urllib
from lxml import html
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scraper(option_dict):
    print(option_dict)

    # r = requests.get('https://www.aniplaylist.com/Mashiro-no-Oto?types=Opening~Ending&markets=United%20States%20of%20America%20(USA)', timeout=(5,20))
    # soup = BeautifulSoup(r.text, 'html.parser')
    # links = soup.findAll('div', class_='column is-3-widescreen is-4-desktop is-6-tablet')
    # print(links)

    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    brower = webdriver.Firefox(firefox_options=fireFoxOptions)

    brower.get('https://pythonbasics.org')
    html = brower.page_source
    soup = BeautifulSoup(html, 'lxml')
    print(soup)

    
if __name__== "__main__":

   # JSON Input for testing purposes

   test_json = {"url": "https://www.aniplaylist.com/Mashiro-no-Oto?types=Opening~Ending&markets=United%20States%20of%20America%20(USA)", "name": "One Piece", "market": "Japan"}
   
   scraper(test_json)