from parsel import Selector
import re
import time
import requests

from tech_news.database import create_news


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
    if html_content is None or html_content == '':
        return None

    selector = Selector(html_content)
    queryString = 'div.nav-links  a.next::attr(href)'
    listStrings = selector.css(queryString).get()
    return listStrings


def scrape_quant_comments(html_content):
    if html_content is None or html_content == '':
        return 0
    selector = Selector(html_content)
    queryString = 'div.post-comments h5.title-block::text'
    comments_text = selector.css(queryString).get()
    if comments_text is None:
        return 0
    quant = re.sub('[^0-9]', '', comments_text)
    comments_count = int(quant)
    return comments_count


# Requisito 4
def scrape_noticia(html_content):
    if html_content is None or html_content == '':
        return None

    selector = Selector(html_content)
    comments_count = scrape_quant_comments(html_content)

    sumQuery = 'div.entry-content'
    return {
        'url': selector.css('link[rel=canonical]::attr(href)').get(),
        'title': selector.css('h1.entry-title::text').get(),
        'timestamp': selector.css('li.meta-date::text').get(),
        'writer': selector.css('a.url::text').get(),
        'comments_count': comments_count,
        'summary': selector.css(sumQuery).xpath('string(//p)').get(),
        'tags': selector.css('a[rel=tag]::text').getall(),
        'category': selector.css('a.category-style span.label::text').get()
    }


def get_all_news(amount):
    allLinks = []
    link = 'https://blog.betrybe.com'
    while True:
        html_content = fetch(link)

        moreNewsLinks = scrape_novidades(html_content)
        allLinks.extend(moreNewsLinks)

        nextLinkPage = scrape_next_page_link(html_content)
        if amount-len(allLinks) > 0:
            link = nextLinkPage
        else:
            break
    return allLinks


# Requisito 5
def get_tech_news(amount):
    allLinks = get_all_news(amount)
    allNews = []
    for i in range(amount):
        html_content = fetch(allLinks[i])
        noticia = scrape_noticia(html_content)
        allNews.append(noticia)
    create_news(allNews)
    return allNews
