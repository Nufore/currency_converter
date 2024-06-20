import requests
from bs4 import BeautifulSoup
from app.core.config import settings


def get_currency_data(from_cur: str, to_cur: str) -> str | float:
    """
    Функция парсит сайт и на основе html тега input с id="answer"
    получаем аттрибут value - курс одной валюты по отношению к другой

    :param from_cur: Код основной валюты
    :param to_cur: Код валюты которую конвертируют
    :return: (str | float), Если статус ответа 200 и существует код валюты, то
    отдаем курс одной валюты по отношению к другой, иначе сообщение об ошибке
    """

    url = f'{settings.base_url}/{from_cur.lower()}/{to_cur.lower()}'
    r = requests.get(url)

    if not r.status_code == 200:
        return "status code is not 200"

    soup = BeautifulSoup(r.text, 'lxml')
    search_input = soup.find(settings.html_tag, {settings.html_attr: settings.html_attr_name})

    if not search_input:
        return "wrong currency code"

    cur_value = float(search_input.attrs['value'])

    return cur_value
