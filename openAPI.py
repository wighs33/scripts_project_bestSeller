import urllib.request
from xml.dom.minidom import parseString
import http.client
import book

client_id = "F5hus3tIzimtuicU0AVm"
client_secret = "MeU8Z5bALM"

conn = http.client.HTTPSConnection("openapi.naver.com")

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

def getBook(typeOfBooks, encText, NumOfBooks):  # type(d_titl, d_auth, d_catg) / keyword / num
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
            parseData = parseString(BooksDoc)
            rssList = parseData.childNodes
            channelList = rssList[0].childNodes
            item = channelList[0]

            subitems = item.childNodes
            bookDataList = []
            for i in range(7, 7 + NumOfBooks):
                bookDataList.append(subitems[i].childNodes)
            bookList = []
            for i in range(NumOfBooks):
                book_ = book.Book()
                book_.setData(bookDataList[i])
                bookList.append(book_)
            conn.close()
            return bookList
    conn.close()