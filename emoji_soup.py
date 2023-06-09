import requests
from bs4 import BeautifulSoup as bs


def get_emoji_data():
    session = requests.Session()
    session.headers['User-Agent'] =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    html = session.get('https://carpedm20.github.io/emoji/')
    print(html)
    
    # create a soup
    soup = bs(html.text, 'html.parser')
    emoji_list = []
    for row in soup.findAll('table')[0].findAll('tr')[2:-1]:
        entry = ':' + row.text.split(':')[1] + ':'
        emoji_list.append(entry)
    return emoji_list