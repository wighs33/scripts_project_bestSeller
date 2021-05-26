import os
import sys
import http.client
import urllib.request
from xml.dom.minidom import parseString
import re

client_id = "F5hus3tIzimtuicU0AVm"
client_secret = "MeU8Z5bALM"

conn = http.client.HTTPSConnection("openapi.naver.com")

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

class Book:
    def __init__(self):
        self.titles = []
        self.links = []
        self.images = []
        self.authors = []
        self.prices = []
        self.discounts = []
        self.publishers = []
        self.pubdates = []
        self.isbns = []
        self.descriptions = []
        self.numberofbooks = 0

    def clearData(self):
        self.titles.clear()
        self.links.clear()
        self.images.clear()
        self.authors.clear()
        self.prices.clear()
        self.discounts.clear()
        self.publishers.clear()
        self.pubdates.clear()
        self.isbns.clear()
        self.descriptions.clear()

    def setData(self, typeOfBooks, encText, NumOfBooks=16):         # d_titl, d_auth, d_catg
        self.clearData()
        encText = urllib.parse.quote(encText)
        if typeOfBooks == "d_catg":
            params = "?display=" + str(NumOfBooks) + "&start=1" + "&sort=count" + "&d_cont=1" + "&d_catg=" + encText
        else:
            params = "?display=" + str(NumOfBooks) + "&start=1" + "&sort=count" + "&" + typeOfBooks + "=" + encText

        conn.request("GET", "/v1/search/book_adv.xml" + params, None, headers)
        res = conn.getresponse()

        if int(res.status) == 200:
            BooksDoc = res.read().decode('utf-8')
            if BooksDoc == None:
                print("에러")
            else:
                # print(parseString(BooksDoc).toprettyxml())
                parseData = parseString(BooksDoc)
                rssList = parseData.childNodes
                channelList = rssList[0].childNodes
                item = channelList[0]

                subitems = item.childNodes
                # print(subitems[7])
                books = []
                for i in range(7, 7 + NumOfBooks):
                    books.append(subitems[i].childNodes)

                for i in range(0, NumOfBooks):
                    self.titles.append(re.sub('(<([^>]+)>)', '', books[i][0].firstChild.nodeValue))
                    self.links.append(books[i][1].firstChild.nodeValue)
                    self.images.append(books[i][2].firstChild.nodeValue)
                    self.authors.append(books[i][3].firstChild.nodeValue)
                    self.prices.append(books[i][4].firstChild.nodeValue)
                    if books[i][5].firstChild:
                        self.discounts.append(books[i][5].firstChild.nodeValue)
                    else:
                        self.discounts.append("")
                    self.publishers.append(books[i][6].firstChild.nodeValue)
                    self.pubdates.append(books[i][7].firstChild.nodeValue)
                    self.isbns.append(books[i][8].firstChild.nodeValue)
                    if books[i][9].firstChild:
                        self.descriptions.append(re.sub('(<([^>]+)>)', '', books[i][9].firstChild.nodeValue))
                    else:
                        self.descriptions.append("")
                self.numberofbooks = len(self.titles)

# b = Book()
# b.setData("d_catg", "100", 16)
# print(b.titles)
# print(b.links)
# print(b.images)
# print(b.authors)
# print(b.prices)
# print(b.discounts)
# print(b.publishers)
# print(b.pubdates)
# print(b.isbns)
# print(b.descriptions)
# print(b.numberofbooks)
