# -*- coding:cp949 -*-
import os
import sys
import http.client
from xml.dom.minidom import parseString
import re
DataList = []

client_id = "F5hus3tIzimtuicU0AVm"
client_secret = "MeU8Z5bALM"

conn = http.client.HTTPSConnection("openapi.naver.com")

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
encText = "love"
params = "?query=" + encText + "&display=10&start=1"

conn.request("GET", "/v1/search/book.xml" + params, None, headers)
res = conn.getresponse()

# if int(res.status) == 200:
#     BooksDoc = res.read().decode('utf-8')
#     print(parseString(BooksDoc).toprettyxml())
# else:
#     print("HTTP Request is failed :" + res.reason)
#     print(res.read().decode('utf-8'))


if int(res.status) == 200:
    BooksDoc = res.read().decode('utf-8')
    if BooksDoc == None:
        print("에러")
    else:
        print(parseString(BooksDoc).toprettyxml())
        parseData = parseString(BooksDoc)
        print(parseData)
        bookInfo = parseData.childNodes
        print(bookInfo)
        row = bookInfo[0].childNodes
        print(row)
        item = row[0]

        print(item.nodeName)
        subitems = item.childNodes
        print(subitems[7])
        books = []
        for i in range(7, 17):
            books.append(subitems[i].childNodes)

        for i in range(0, 10):
            booksTitle = re.sub('(<([^>]+)>)', '', books[i][0].firstChild.nodeValue)
            print(booksTitle)
        # for book in subitems[7].childNodes:
        #     print(book)
        #     print(book.firstChild.nodeValue)
        # for book in subitems[8].childNodes:
        #     print(book)
        #     print(book.firstChild.nodeValue)
            # print(subitems[1])
            # print(subitems[1].firstChild.nodeValue)
            # print(subitems[2])
            # print(subitems[2].firstChild.nodeValue)
            # print(subitems[3])
            # print(subitems[3].firstChild.nodeValue)
            # print(subitems[4])
            # print(subitems[4].firstChild.nodeValue)
            # print(subitems[5])
            # print(subitems[5].firstChild.nodeValue)
            # print(subitems[6])
            # print(subitems[6].firstChild.nodeValue)
            # print(subitems[7])
            # print(subitems[7].firstChild.nodeValue)
            # print(subitems[8])
            # print(subitems[8].firstChild.nodeValue)
            # print(subitems[9])
            # print(subitems[9].firstChild.nodeValue)
            # print(subitems[10])
            # print(subitems[10].firstChild.nodeValue)
            # print(subitems[11])
            # print(subitems[11].firstChild.nodeValue)
            # print(subitems[12])
            # print(subitems[12].firstChild.nodeValue)
            # print(subitems[13])
            # print(subitems[13].firstChild.nodeValue)
            # print(subitems[14])
            # print(subitems[14].firstChild.nodeValue)
            # print(subitems[15])
            # print(subitems[15].firstChild.nodeValue)

            # if subitems[3].firstChild.nodeValue == InputLabel.get():  # 援??대???媛?? 寃쎌?
            #     pass
            # elif subitems[5].firstChild.nodeValue == InputLabel.get():  # ???대???媛?? 寃쎌?
            #     pass
            # else:
            #     continue
            #
            # if subitems[29].firstChild is not None:
            #     tel = str(subitems[29].firstChild.nodeValue)
            #     pass  # ???
            #     if tel[0] != '0':
            #         tel = "02-" + tel
            #         pass
            #     DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
            # else:
            #     DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))
        #
        # for i in range(len(DataList)):
        #     RenderText.insert(INSERT, "[")
        #     RenderText.insert(INSERT, i + 1)
        #     RenderText.insert(INSERT, "] ")
        #     RenderText.insert(INSERT, "시설명: ")
        #     RenderText.insert(INSERT, DataList[i][0])
        #     RenderText.insert(INSERT, "굈")
        #     RenderText.insert(INSERT, "주소: ")
        #     RenderText.insert(INSERT, DataList[i][1])
        #     RenderText.insert(INSERT, "굈")
        #     RenderText.insert(INSERT, "전화번호: ")
        #     RenderText.insert(INSERT, DataList[i][2])
        #     RenderText.insert(INSERT, "굈굈")

conn.close()