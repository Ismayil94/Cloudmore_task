import requests
from bs4 import BeautifulSoup


def get_menu_links(url):
    links = {}
    req = requests.get(url)
    data = req.text

    soup = BeautifulSoup(data, features="html.parser")
    for link in soup.select("li[class*='hs-menu-depth-'].hs-menu-item > a"):
        links[link.get_text().lower()] = link.get('href')
    return links


if __name__ == "__main__":
    print("It is not for running!")
