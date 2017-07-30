# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html,"lxml")
#
# nameList = bsObj.findAll("span",{"class":"green"})
#
# for name in nameList:
#     print(name.get_text())


# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html,"lxml")
# for child in bsObj.find("table",{"id":"giftList"}).children:
#     print(child)

# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)

# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"
#                         }).parent.previous_sibling.get_text())

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])