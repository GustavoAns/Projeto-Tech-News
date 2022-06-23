from collections import Counter
from tech_news.database import search_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    result = list(search_news({}))
    result.sort(key=itemgetter("comments_count"))
    result = result[-5:]
    listTuplas = []
    for news in reversed(result):
        listTuplas.append((news["title"], news["url"]))
    return listTuplas


# Requisito 11
def top_5_categories():
    result = list(search_news({}))
    newsObjs = []

    for news in result:
        newsObjs.append(news["category"])

    tupla = Counter(newsObjs).most_common(5)
    return [name[0] for name in tupla]
