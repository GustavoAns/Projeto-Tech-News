# Requisito 6
from datetime import datetime
from tech_news.database import search_news

MES = {
    '01': "janeiro",
    '02': "fevereiro",
    '03': "março",
    '04': "abril",
    '05': "maio",
    '06': "junho",
    '07': "julho",
    '08': "agosto",
    '09': "setembro",
    '10': "outubro",
    '11': "novembro",
    '12': "dezembro"
}


def search_by_title(title):
    result = list(search_news({"title": {"$regex": title, '$options': 'i'}}))
    listTuplas = []
    for news in result:
        listTuplas.append((news["title"], news["url"]))
    return listTuplas


# Requisito 7
# https://docs.python.org/3/library/datetime.html
#   - fromisoformat / string para datetime
# https://pt.stackoverflow.com/questions/8317/como-fazer-a-fun%C3%A7%C3%A3o-date-formatar-uma-data-em-portugu%C3%AAs
#   - como fazer a função strftime formatar uma data em "português" - strftime
# https://www.w3schools.com/php/func_string_setlocale.asp - setlocale()

def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Data inválida')
    numbers = date.split('-')
    newDate = f'{(int(numbers[2]))} de {MES[numbers[1]]} de {numbers[0]}'
    result = list(
        search_news({"timestamp": {"$regex": newDate, '$options': 'i'}})
    )
    listTuplas = []
    for news in result:
        listTuplas.append((news["title"], news["url"]))
    return listTuplas


# Requisito 8
def search_by_tag(tag):
    result = list(
        search_news({"tags": {"$regex": tag, '$options': 'i'}})
    )
    listTuplas = []
    for news in result:
        listTuplas.append((news["title"], news["url"]))
    return listTuplas


# Requisito 9
def search_by_category(category):
    result = list(
        search_news({"category": {"$regex": category, '$options': 'i'}})
    )
    listTuplas = []
    for news in result:
        listTuplas.append((news["title"], news["url"]))
    return listTuplas

