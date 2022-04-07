import requests
import json
from bs4 import BeautifulSoup 

URL = 'https://www.sulpak.kg/f/smartfoniy'
JSON = 'sulpak.json'
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'
}

def parser(url):
    response = requests.get(url, headers=HEADERS, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('li', class_='tile-container')
    tabs = []

    for item in items:
        tabs.append({
            'Названия' : item.find('h3', class_ = 'title').get_text(strip=True),
            'Цена' : item.find('div', class_ = 'price').get_text(strip=True),
            'Фото' : item.find('img').get('src'),
            'Статус' : item.find('span', class_ = 'availability').get_text(strip=True),
            'Код Товара' : item.find('span', class_ = 'code').get_text(strip=True),
        })

    with open('sulpak.json', 'w') as file:
        json.dump(tabs, file, indent=4, ensure_ascii=False)

def main():
    parser(URL)

if __name__ == "__main__":
    main()

