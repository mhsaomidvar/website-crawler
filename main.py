import requests
from bs4 import BeautifulSoup

target_input = input("input your target website: ")
target_url = "https://" + target_input
foundLinks = []


def make_request(url):
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def crawl(url):
    links = make_request(url)
    for link in links.find_all('a'):
        founded_link = link.get("href")
        if founded_link:
            if "#" in founded_link:
                founded_link = founded_link.split("#")[0]
            if target_url in founded_link and founded_link not in foundLinks:
                foundLinks.append(founded_link)
                print(founded_link)
                # recursive
                crawl(founded_link)


crawl(target_url)


# html parsing


