import requests
from bs4 import BeautifulSoup
url="https://www.facebook.com"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
title=soup.title
paras=soup.find_all('p')
anchors=soup.find_all('a')
# print(soup.find('p'))
# print(soup.find('p')['class'])
# print(soup.find_all('p',class_='lead'))
# print(soup.find('p').get_text())
# print(soup.get_text())
all_links=set()

for link in anchors:
    if link.get('href')!="#":
        link_Text="https://www.facebook.com"+link.get('href')
        all_links.add(link_Text)
        # print(link_Text)
navbarSupportedContent=soup.find(id="navbarSupportedContent")
# print(navbarSupportedContent.contents)
# for ele in navbarSupportedContent.contents:
#     
    # print(ele)
# .contents - A tag's children are available as list
# .children - A tag's children are available as generator
# for item in navbarSupportedContent.strings:
#     print(item)
# for item in navbarSupportedContent.stripped_strings:
#     print(item)
# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents:
#     print(item.name)
# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.prev_sibling.prev_sibling)
