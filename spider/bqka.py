import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import unquote


def fetch_page(url):
    try:
        response = requests.get(url, headers=py_headers, timeout=60)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None


def getContent(html):
    soup = BeautifulSoup(html, 'html.parser')
    div_content = soup.find('div', class_='content')
    title = div_content.find('h1', class_='wap_none').contents[0]
    
    div_content = soup.find('div', id='chaptercontent')
    div_content.find('p', class_='readinline').decompose()
    remaining_content = ''.join(str(content) for content in div_content.contents)
    remaining_content = title + "\r\n" + remaining_content
    result = remaining_content.replace('"', '').replace('<br>', '\n').replace('<br/>', '\n')    
    return result


def main():
    html = fetch_page(novel_url)
    soup = BeautifulSoup(html, 'html.parser')
    dd_last_tag = soup.find('div', class_="listmain").find_all('dd', class_=False)[-1]
    maxNovel = int(dd_last_tag.find('a').get('href').split('/')[-1].split('.')[0])

    for i in range(457, maxNovel+1):
        href = '{}/{}.html'.format(novel_url, i)
        html = fetch_page(href)
        print('开始抓取：' + href)
        content = getContent(html)
        with open("D:\\Users\\Administrator\\Desktop\\novel\\"+novel_title+".txt", "a", encoding="utf-8") as file:
            file.write(str(content))

py_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

novel_url = 'https://www.bqka.cc/book/6853'
novel_title = '七界传说'

if __name__ == "__main__":
    main()
