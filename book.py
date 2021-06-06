import re

class Book:
    def __init__(self):
        self.title = ''
        self.link = ''
        self.image = ''
        self.author = ''
        self.price = ''
        self.pubdate = ''
        self.description = ''
        self.favorites = False      # 즐겨찾기 여부
    def setData(self, data):
        self.title = re.sub('(<([^>]+)>)', '', data[0].firstChild.nodeValue)
        self.link = data[1].firstChild.nodeValue
        self.image = data[2].firstChild.nodeValue if data[2].firstChild else ''
        self.author = re.sub('(<([^>]+)>)', '', data[3].firstChild.nodeValue)
        self.price = data[4].firstChild.nodeValue
        self.pubdate = data[7].firstChild.nodeValue
        self.description = re.sub('(<([^>]+)>)', '', data[9].firstChild.nodeValue) if data[9].firstChild else ''
        self.description = self.description.replace("&#x0D;", " ")