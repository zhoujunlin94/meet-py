import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import unquote


def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def getMaxPage(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('span', class_='pagination')
    if pagination:
        last_page_link = pagination.find_all('a', class_='page-number')[-1]
        if last_page_link:
            last_page_href = last_page_link.get('href')
            # 使用正则表达式从href中提取数字
            match = re.search(r'/page/(\d+)/', last_page_href)
            if match:
                return int(match.group(1))
    return None

def gethrefs(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 找到所有的a标签
    a_tags = soup.find_all('a', class_='list-group-item list-group-item-action')
    
    # print(a_tags)

    # 提取每个a标签的href属性
    hrefs = [a.get('href') for a in a_tags]
    return hrefs

def getMarkdownBody(html):

    soup = BeautifulSoup(html, 'html.parser')

    # 找到所有的a标签
    markdownBody = soup.find_all('div', class_='markdown-body')

    return str(markdownBody[0])

def main():
    url = 'https://onehu.xyz/archives/'  
    html = fetch_page(url)
    maxPage = getMaxPage(html) + 1

    url_template = 'https://onehu.xyz/archives/page/{}/#board'  
    for i in range(1, 2):
        if i > 1:
            url = url_template.format(i)
        # print(url)
        html = fetch_page(url)
        # print(html)
        if html:
            hrefs = gethrefs(html)
            # print(hrefs)
            for href in hrefs:
                href = unquote(href)
                posts_url = 'https://onehu.xyz' + href
                posts_html = fetch_page(posts_url)

                # print(posts_html)

                title = posts_url.rsplit('/', 1)[-1]
                
                postsContent = getMarkdownBody(posts_html)
            
                with open("D:\\Users\\Administrator\\Desktop\\zhihu\\" +title + ".md", "w", encoding="utf-8") as file:
                    file.write(str(postsContent))

        else:
            print(f"Failed to fetch page {i}")


if __name__ == "__main__":
    main()
