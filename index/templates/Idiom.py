from bs4 import BeautifulSoup as bs
import urllib.request as ur

url = 'https://ko.dict.naver.com/#/topic/search?category1=idiom'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
tag = soup.find_all('div', {"class":"orgin"})

url2 = 'https://ko.dict.naver.com/#/topic/search?category1=idiom'
html2 = ur.urlopen(url)
soup2 = bs(html.read(), 'html.parser')
tag2 = soup.find_all('ul', {"class":"mean.list"})
