from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import requests
from webdriver_manager.chrome import ChromeDriverManager
import json
from flask import Flask
import urllib.request


application = Flask(__name__)


@application.route('/')
def index() -> str:
    """
    Check internet connection
    :return: status
    """
    try:
        urllib.request.urlopen('https://www.google.com/')
        return "Services are up & running!"
    except:
        return "Connection Error"


@application.route('/getRandomMeme')
def get_random_meme() -> str:
    """
    :return: URL to image
    """
    print("get_random_meme() requested")

    CONNECTION_ERROR = "https://memegenerator.net/img/instances/65524138/connection-error-i-feel-so-rejected.jpg"
    uri = "https://meme-api.herokuapp.com/gimme"
    try:
        u_response = requests.get(uri)
    except requests.ConnectionError:
        print("Connection error")
        return CONNECTION_ERROR
    j_response = u_response.text
    data = json.loads(j_response)
    return data["url"]


@application.route('/getSpecificMeme/<keyword>')
def get_specific_meme(keyword: str) -> str:
    """
    :param keyword: keyword to split
    :return: URL to image
    """
    print("get_specific_meme() requested for", keyword)

    BASE_URL = 'https://memes.com/search/?term='
    MEME_LIST_CLASS = 'pt-5 js-post-tiles-container js-search-feed d-flex flex-wrap justify-content-between post-tile-row'
    BASE_MEME_URL = "https://memes.com"
    MEME_CLASS = 'post-media-container'
    UNABLE_TO_LOAD = 'https://i.kym-cdn.com/photos/images/newsfeed/001/668/803/f75.jpg'

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
    for i in list_memes[:5]:
        if i['href'] is not None:
            hrefs.append(i['href'])
    print('Random meme hrefs', hrefs)

    # In case not able to retrieve details, return unable to load
    if len(hrefs) == 0:
        return UNABLE_TO_LOAD

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


@application.route('/getUrban/<choice>/<keyword>')
def get_urban_definition(choice: str, keyword: str) -> str:
    """
    :param keyword: keyword to split
    :return: Meaning text
    """
    print("get_urban_definition() requested for ", choice, keyword)

    NOT_FOUND = 'https://i.imgflip.com/1k5gq1.jpg'
    BASE_URBAN_URL = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    keyword = ' '.join(keyword.split())
    
    querystring = {"term": keyword}
    headers = {
        'x-rapidapi-key': "5ed327aae2msh24174280b4e39a5p10a7f4jsn69ad8ec56ff4",
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    response = requests.request("GET", BASE_URBAN_URL, headers=headers, params=querystring)
    definitions = json.loads(response.text)['list']

    # If no definition found
    if len(definitions) == 0:
        return NOT_FOUND

    req = None
    if choice == "definition":
        req = definitions[0]['definition']
    elif choice == "sound":
        req_list = definitions[0]['sound_urls']
        if len(req_list) == 0:
            return "SOUND_NOT_FOUND"
        else:
            req = req_list[0]
    else:
        raise Exception("Invalid request")
    return req

if __name__ == "__main__":
    application.run()
