
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

import requests
import bs4

HEADERS = {'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru,en;q=0.9,fr;q=0.8',
'Connection': 'keep-alive',
'Cookie': '_ym_d=1652004307; _ym_uid=16520043071036031421; fl=ru; hl=ru; _ga=GA1.2.1408891750.1652004308; habr_web_home_feed=/all/; _ym_isad=2; _gid=GA1.2.358542480.1661955765; _gat_gtag_UA_726094_1=1',
'Host': 'habr.com',
'sec-ch-ua-platform': 'Windows',
'Sec-Fetch-Dest': 'script',
'Sec-Fetch-Mode': 'no-cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'}


request = requests.get('https://habr.com/ru/all/', headers=HEADERS)
soup = bs4.BeautifulSoup(request.text, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')
for article in articles:
    hub_l = {hub.find('a').text.removesuffix('*').strip().lower() for hub in article.find_all(class_='tm-article-snippet__hubs-item')}
    if hub_l & KEYWORDS:
        article_time = article.find('time')
        art_t = article_time.attrs['title']
        title_title = article.find('h2').find('a')
        title = title_title.text
        href = 'https://habr.com/ru/all/' + title_title.attrs['href']
        print(f' {art_t} --> {title} --> {href}')
        print('------------------------------------')