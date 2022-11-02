import requests
from bs4 import BeautifulSoup


def get_exchange_rate(target1, target2):
    headers = {"User=Agent": "Mozilla/5.0", "Content-Type": "text/html; charset=utf-8"}
    response = requests.get(
        f"https://kr.investing.com/currencies/{target1}-{target2}", headers=headers
    )
    content = BeautifulSoup(response.text, "html.parser")
    containers = content.select("span", {"data-test": "instrument-price-last"})

    print(containers)


get_exchange_rate("usd", "krw")
