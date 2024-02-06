from bs4 import BeautifulSoup
import requests
import validators


def get_soup(link: str) -> BeautifulSoup | None:
    if not validators.url(link):
        return None
    with requests.Session() as s:
        res = s.get(link, timeout=10, verify=False)
    # print(res.content)
    soup = BeautifulSoup(res.content, "lxml")
    # print(soup)

    return soup


def get_title(soup: BeautifulSoup, selector: str) -> str | None:
    if not isinstance(soup, BeautifulSoup):
        return None
    title = soup.select_one(selector)
    return title.text.strip() if title and title.text else None


def get_paragraphs(soup: BeautifulSoup, selector: str) -> str | None:
    if not isinstance(soup, BeautifulSoup):
        return None
    paragraph = soup.select_one(selector)
    # print(paragraphs)
    # paragraph = paragraph.text.strip()
    # print(paragraph)
    return paragraph.text.strip() if paragraph and paragraph.text else None


def get_links(base_url: str) -> list[str]:
    res = requests.get(base_url)
    soup = BeautifulSoup(res.content, "html.parser")
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))
    return links
