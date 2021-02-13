import requests
import json
from main import application


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
