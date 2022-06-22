from parsel import Selector
import time
import requests


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        headers = {'User-Agent': 'Fake user-agent'}
        response = requests.get(url, timeout=3, headers=headers)
        response.raise_for_status()  # raise exception if not 200
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    if html_content is None or html_content == '':
        return []

    selector = Selector(html_content)
    queryString = 'div.post-outer div.post-inner '\
        'header.entry-header h2.entry-title a::attr(href)'
    listStrings = selector.css(queryString).getall()
    return listStrings


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
