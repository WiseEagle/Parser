from bs4 import BeautifulSoup as BS
import requests
import re

cookies = {
    'OCSESSID': '6cc48eafb46d9422ebeaa27693',
    'language': 'uk-ua',
    'currency': 'UAH',
    '_gcl_au': '1.1.1272537833.1716799182',
    '_ga': 'GA1.1.1247072547.1716799182',
    'SLG_G_WPT_TO': 'uk',
    'twk_idm_key': 'DOO3S1PCvZtx3D0t-TqOr',
    'SLG_GWPT_Show_Hide_tmp': '1',
    'SLG_wptGlobTipTmp': '1',
    '_ga_TELSBE7996': 'GS1.1.1716905462.2.0.1716905462.0.0.0',
    'TawkConnectionTime': '0',
    'twk_uuid_5d6c33b0eb1a6b0be60a6fe4': '%7B%22uuid%22%3A%221.1vX9zw7larvbpEmH6a6hcbvq8gdPXWl5xXOMCg7L0WX329YyxKGDYerTp0Pbj68WwkUfZlzhyFGi2gIfbdcHuBx0urinNc9aXIITqb2iHg5p786UNHvl1SH%22%2C%22version%22%3A3%2C%22domain%22%3A%22bezpeka.zp.ua%22%2C%22ts%22%3A1716905464331%7D',
    'biatv-cookie': '{%22firstVisitAt%22:1716799186%2C%22visitsCount%22:2%2C%22currentVisitStartedAt%22:1716905462%2C%22currentVisitLandingPage%22:%22https://bezpeka.zp.ua/%22%2C%22currentVisitUpdatedAt%22:1716905462%2C%22currentVisitOpenPages%22:1%2C%22campaignTime%22:1716799186%2C%22campaignCount%22:1%2C%22utmDataCurrent%22:{%22utm_source%22:%22(direct)%22%2C%22utm_medium%22:%22(none)%22%2C%22utm_campaign%22:%22(direct)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20set)%22%2C%22beginning_at%22:1716799186}%2C%22utmDataFirst%22:{%22utm_source%22:%22(direct)%22%2C%22utm_medium%22:%22(none)%22%2C%22utm_campaign%22:%22(direct)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20set)%22%2C%22beginning_at%22:1716799186}}',
    'bingc-activity-data': '{%22numberOfImpressions%22:1%2C%22activeFormSinceLastDisplayed%22:0%2C%22pageviews%22:1%2C%22callWasMade%22:0%2C%22updatedAt%22:1716907681}',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'uk,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'OCSESSID=6cc48eafb46d9422ebeaa27693; language=uk-ua; currency=UAH; _gcl_au=1.1.1272537833.1716799182; _ga=GA1.1.1247072547.1716799182; SLG_G_WPT_TO=uk; twk_idm_key=DOO3S1PCvZtx3D0t-TqOr; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; _ga_TELSBE7996=GS1.1.1716905462.2.0.1716905462.0.0.0; TawkConnectionTime=0; twk_uuid_5d6c33b0eb1a6b0be60a6fe4=%7B%22uuid%22%3A%221.1vX9zw7larvbpEmH6a6hcbvq8gdPXWl5xXOMCg7L0WX329YyxKGDYerTp0Pbj68WwkUfZlzhyFGi2gIfbdcHuBx0urinNc9aXIITqb2iHg5p786UNHvl1SH%22%2C%22version%22%3A3%2C%22domain%22%3A%22bezpeka.zp.ua%22%2C%22ts%22%3A1716905464331%7D; biatv-cookie={%22firstVisitAt%22:1716799186%2C%22visitsCount%22:2%2C%22currentVisitStartedAt%22:1716905462%2C%22currentVisitLandingPage%22:%22https://bezpeka.zp.ua/%22%2C%22currentVisitUpdatedAt%22:1716905462%2C%22currentVisitOpenPages%22:1%2C%22campaignTime%22:1716799186%2C%22campaignCount%22:1%2C%22utmDataCurrent%22:{%22utm_source%22:%22(direct)%22%2C%22utm_medium%22:%22(none)%22%2C%22utm_campaign%22:%22(direct)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20set)%22%2C%22beginning_at%22:1716799186}%2C%22utmDataFirst%22:{%22utm_source%22:%22(direct)%22%2C%22utm_medium%22:%22(none)%22%2C%22utm_campaign%22:%22(direct)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20set)%22%2C%22beginning_at%22:1716799186}}; bingc-activity-data={%22numberOfImpressions%22:1%2C%22activeFormSinceLastDisplayed%22:0%2C%22pageviews%22:1%2C%22callWasMade%22:0%2C%22updatedAt%22:1716907681}',
    'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
}

site_name = 'https://bezpeka.zp.ua'

r = requests.get(site_name, cookies=cookies, headers=headers)


# URL страницы для парсинга
# r = requests.get(response.url, cookies=cookies, headers=headers)

print(r.status_code)


def get_categorys_paginate_links(link):
    # Отправка GET-запроса на страницу

    pr = requests.get(link)

    print(pr.status_code)
    # Проверка успешности запроса
    if pr.status_code == 200:

        # Получение содержимого страницы
        html_content = pr.content

        # Парсинг HTML с использованием BeautifulSoup
        page_soup = BS(html_content, 'html.parser')

        pagination = page_soup.find('ul', class_='pagination')

        # Извлечение категорий и ссылок на них
        links = []
        if pagination is None:
            return False
        else:
            for a_tag in pagination.find_all('a'):
                if a_tag.text.isdigit():
                    links.append(a_tag['href'])

            return links
    else:
        print('Error paginate links')


def print_categorys_to_file(filename, names, links):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('{\n')

    # write categoryes to  json file
    for name, link in zip(names, links):
        # if last element
        if not link.startswith('http') and not link.startswith('https'):
            continue

        paginate_links = get_categorys_paginate_links(link)

        if name == names[-1]:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f'"{name}": "{link}"\n')
        else:
            if paginate_links:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(f'"{name}": ["{link}",\n')
                    for l in paginate_links:
                        if l == paginate_links[-1]:
                            file.write(f'"{l}"\n')
                        else:
                            file.write(f'"{l}",\n')
                    file.write('],\n')
            else:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(f'"{name}": "{link}",\n')

    with open(filename, 'a', encoding='utf-8') as file:
        file.write('}\n')


if r.status_code == 200:

    # Получение содержимого страницы
    html_content = r.content

    # Парсинг HTML с использованием BeautifulSoup
    soup = BS(html_content, 'html.parser')

    # Извлечение категорий и ссылок на них
    a_tags = soup.find_all('a', class_='rm-menu-list-item-link')

    names = []
    links = []

    for a_tag in a_tags:

        names = names + \
            [a_tag.find('span', class_='rm-menu-list-item-name').text]
        links = links + [a_tag['href']]

    filename = 'categoryes.json'
    print_categorys_to_file(filename, names, links)

else:
    print('Error')
