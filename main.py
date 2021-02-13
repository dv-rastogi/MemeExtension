from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import requests
from webdriver_manager.chrome import ChromeDriverManager
import json
from flask import Flask

BASE_URL = 'https://memes.com/search/?term='
MEME_LIST_CLASS = 'pt-5 js-post-tiles-container js-search-feed d-flex flex-wrap justify-content-between post-tile-row'
BASE_MEME_URL = "https://memes.com"
MEME_CLASS = 'post-media-container'
RECURSION_LIMIT = 3

application = Flask(__name__)


@application.route('/')
def index():
    return "Services are up & running!"


@application.route('/getRandomMeme')
def get_random_meme():
    uri = "https://meme-api.herokuapp.com/gimme"
    try:
        u_response = requests.get(uri)
    except requests.ConnectionError:
        return "Connection Error"
    j_response = u_response.text
    data = json.loads(j_response)
    return data["url"]


@application.route('/getSpecificMeme/<keyword>')
def get_specific_meme(keyword: str, depth=0) -> str:
    """
    :param depth: Recursion depth
    :param keyword: keyword to split
    :return: URL to image
    """

    if depth > RECURSION_LIMIT:
        raise Exception("Not able to retrieve images")

    init_url = BASE_URL + '+'.join(keyword.split())
    print('URL formed', init_url)

    """
    Scrape a meme url from list of memes
    https://stackoverflow.com/questions/52687372/beautifulsoup-not-returning-complete-html-of-the-page/52688147
    Wait for the page to load as selected memes are queried

    Save chrome driver in cache
    https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path
    """
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(init_url)
    time.sleep(3)
    init_page = driver.page_source
    driver.quit()

    soup = BeautifulSoup(init_page, 'html.parser')
    list_memes_section = soup.find(class_=MEME_LIST_CLASS)
    list_memes = list_memes_section.findAll("a")
    hrefs = []
    for i in list_memes:
        if i['href'] is not None:
            hrefs.append(i['href'])
    print('Random meme hrefs', hrefs)

    # In case not able to retrieve details, recurse
    if len(hrefs) == 0:
        get_specific_meme(keyword, depth + 1)

    """
    Obtain the actual image of meme using another scrape
    """
    meme_url = BASE_MEME_URL + random.choice(hrefs)
    print("Selected meme", meme_url)

    page = requests.get(meme_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    meme_link_holder_parent = soup.find(class_=MEME_CLASS)
    meme_link_holder = meme_link_holder_parent.find('img')
    meme_link = meme_link_holder['src']
    return meme_link


if __name__ == "__main__":
    application.run()
