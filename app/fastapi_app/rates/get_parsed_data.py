import requests
from bs4 import BeautifulSoup
from app.core.config import settings


def get_currency_data(from_cur: str, to_cur: str, value: str) -> str | float:
    url = f'{settings.base_url}/{from_cur.lower()}/{to_cur.lower()}'
    r = requests.get(url)

    if not r.status_code == 200:
        return "status code is not 200"

    search_input = BeautifulSoup(r.text, 'lxml').find("input", {"id": "answer"})

    if not search_input:
        return "wrong currency code"

    cur_value = search_input.attrs['value']
    result_value = round(float(cur_value), 2) * float(value)

    return result_value
