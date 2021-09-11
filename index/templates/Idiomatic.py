from bs4 import BeautifulSoup as bs
import urllib.request as ur
while True:  # 무한 입력받기
    url = 'https://ko.dict.naver.com/#/topic/search?category1=phrase'
    html = ur.urlopen(url)
    soup = bs(html.read(), 'html.parser')
    tag = soup.find_all('div', {"class":"orgin"})

    url2 = 'https://ko.dict.naver.com/#/topic/search?category1=phrase'
    html2 = ur.urlopen(url)
    soup2 = bs(html.read(), 'html.parser')
    tag2 = soup.find_all('ul', {"class":"mean.list"})

    for Idiomatics in tag:
        with open('Idiomatics.html', 'w') as f:
            f.write('<html><body>')
            for w in Idiomatics:
                f.write(w+'<br>')
            f.write('</body></html>')
