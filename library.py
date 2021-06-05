import re

class Library:
    def __init__(self):
        self.title = ''
        self.mapx = ''
        self.mapy = ''
    def setData(self, data):
        self.title = re.sub('(<([^>]+)>)', '', data[7].firstChild.nodeValue)
        self.mapx = data[10].firstChild.nodeValue
        self.mapy = data[11].firstChild.nodeValue