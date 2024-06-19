from bs4 import BeautifulSoup as BS
import requests
import re
import json

cookies = {
    'uuid': 'bc3f558986caa2bfc1b7f3be60083bba',
    '_gcl_au': '1.1.1016944907.1715765773',
    'SLG_G_WPT_TO': 'uk',
    'SLG_GWPT_Show_Hide_tmp': '1',
    'SLG_wptGlobTipTmp': '1',
    'PHPSESSID': '62de36fcc3a87281472f3cb547dfd020',
    '_gid': 'GA1.3.1856742186.1716796057',
    '_ga_H4W7NKV8PR': 'GS1.1.1716796057.3.1.1716796072.45.0.0',
    '_ga': 'GA1.3.2056321501.1715765773',
    'biatv-cookie': '{%22firstVisitAt%22:1715765773%2C%22visitsCount%22:2%2C%22currentVisitStartedAt%22:1716796062%2C%22currentVisitLandingPage%22:%22https://euroservis.com.ua/ua/%22%2C%22currentVisitUpdatedAt%22:1716796077%2C%22currentVisitOpenPages%22:3%2C%22campaignTime%22:1715765773%2C%22campaignCount%22:1%2C%22utmDataCurrent%22:{%22utm_source%22:%22(direct)%22%2C%22utm_medium%22:%22(none)%22%2C%22utm_campaign%22:%22(direct)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20set)%22%2C%22beginning_at%22:1715765773}%2C%22utmDataFirst%22:{%22utm_source%22:%22(direct)%22%2C%22utm_medium%22:%22(none)%22%2C%22utm_campaign%22:%22(direct)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20set)%22%2C%22beginning_at%22:1715765773}}',
    'bingc-activity-data': '{%22numberOfImpressions%22:1%2C%22activeFormSinceLastDisplayed%22:0%2C%22pageviews%22:3%2C%22callWasMade%22:0%2C%22updatedAt%22:1716797260}',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'uk,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'uuid=bc3f558986caa2bfc1b7f3be60083bba; _gcl_au=1.1.1016944907.1715765773; SLG_G_WPT_TO=uk; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; PHPSESSID=62de36fcc3a87281472f3cb547dfd020; _gid=GA1.3.1856742186.1716796057; _ga_H4W7NKV8PR=GS1.1.1716796057.3.1.1716796072.45.0.0; _ga=GA1.3.2056321501.1715765773; biatv-cookie={%22firstVisitAt%22:1715765773%2C%22visitsCount%22:2%2C%22currentVisitStartedAt%22:1716796062%2C%22currentVisitLandingPage%22:%22https://euroservis.com.ua/ua/%22%2C%22currentVisitUpdatedAt%22:1716796077%2C%22currentVisitOpenPages%22:3%2C%22campaignTime%22:1715765773%2C%22campaignCount%22:1%2C%22utmDataCurrent%22:{%22utm_source%22:%22(direct)%22%2C%22utm_medium%22:%22(none)%22%2C%22utm_campaign%22:%22(direct)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20set)%22%2C%22beginning_at%22:1715765773}%2C%22utmDataFirst%22:{%22utm_source%22:%22(direct)%22%2C%22utm_medium%22:%22(none)%22%2C%22utm_campaign%22:%22(direct)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20set)%22%2C%22beginning_at%22:1715765773}}; bingc-activity-data={%22numberOfImpressions%22:1%2C%22activeFormSinceLastDisplayed%22:0%2C%22pageviews%22:3%2C%22callWasMade%22:0%2C%22updatedAt%22:1716797260}',
    'referer': 'https://euroservis.com.ua/ua/',
    'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
}


def get_products_prices():
    if response.status_code == 200:

        # Получение содержимого страницы
        html_content = response.content

        # Парсинг HTML с использованием BeautifulSoup
        soup = BS(html_content, 'html.parser')

        # Извлечение цен (замените 'your-price-selector' на реальный CSS-селектор)
        names = soup.select('.rm-module-title')
        prices = soup.select('.rm-module-price')

        with open('prices.json', 'w', encoding='utf-8') as file:
            file.write('{\n')

        # Обработка и вывод цен
        for name, price in zip(names, prices):
            print(price.text.strip().replace(" грн", "").replace(" ", ""))
            with open('prices.json', 'a', encoding='utf-8') as file:
                # make json
                p = price.text.strip().replace(" грн", "").replace(" ", "")

                file.write('  "name": "' + name.text.strip() + '",\n')
                file.write('  "price": "' + p + '"\n')

        with open('prices.json', 'a', encoding='utf-8') as file:
            file.write('},\n')

    else:
        print('Failed to retrieve the page')


# *****************************************************
data = {}

with open('categoryes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for key, value in data.items():
    # Проверяем, является ли значение строкой
    if isinstance(value, str):
        response = requests.get(
            value,
            cookies=cookies,
            headers=headers,
        )
        get_products_prices()

    # Проверяем, является ли значение списком
    elif isinstance(value, list):
        for link in value:
            response = requests.get(
                link,
                cookies=cookies,
                headers=headers,
            )
            get_products_prices()

    else:
        print(f"Неизвестный тип данных для ключа {key}: {value}")

# *****************************************************

 # type: ignore
