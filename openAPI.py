import urllib.request
from xml.dom.minidom import parseString
import http.client
from book import *
from library import *

client_id = "F5hus3tIzimtuicU0AVm"
client_secret = "MeU8Z5bALM"

def parsing(doc, n):
    parseData = parseString(doc)
    rssList = parseData.childNodes
    channelList = rssList[0].childNodes
    item = channelList[0]
    subitems = item.childNodes

    total = int(subitems[4].firstChild.nodeValue)  # 4번 - total(검색 결과)
    if total < n:  # 검색결과(total)가 출력을 원하는 개수(n)보다 작으면 검색결과만큼만 책 반환
        n = total

    dataList = []
    for i in range(7, 7 + n):
        dataList.append(subitems[i].childNodes)
    return dataList, n

def getBook(typeOfBooks, encText, NumOfBooks):  # type(d_titl, d_auth, d_catg) / keyword / num
    conn = http.client.HTTPSConnection("openapi.naver.com")
    headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

    encText = urllib.parse.quote(encText)
    if typeOfBooks == "d_catg":
        params = "?display=" + str(NumOfBooks) + "&start=1" + "&sort=count" + "&d_cont=1" + "&d_catg=" + encText
    else:
        params = "?display=" + str(NumOfBooks) + "&start=1" + "&sort=count" + "&" + typeOfBooks + "=" + encText

    conn.request("GET", "/v1/search/book_adv.xml" + params, None, headers)
    res = conn.getresponse()

    bookList = []

    if int(res.status) != 200:
        print("에러")
        conn.close()
        return bookList

    booksDoc = res.read().decode('utf-8')
    if booksDoc == None:
        print("에러")
        conn.close()
        return bookList

    bookDataList = parsing(booksDoc, NumOfBooks)[0]
    NumOfBooks = parsing(booksDoc, NumOfBooks)[1]
    for i in range(NumOfBooks):
        book_ = Book()
        book_.setData(bookDataList[i])
        bookList.append(book_)
    conn.close()
    return bookList

def getLibrary(encText, nLibraries):
    conn = http.client.HTTPSConnection("dapi.kakao.com")
    rest_api_key = '313563c3f07e8c05e573185c12ba6164'
    headers = {'Authorization': 'KakaoAK ' + rest_api_key}

    encText += " 도서관"
    encText = urllib.parse.quote(encText)
    params = "?size=" + str(nLibraries) + "&query=" + encText

    conn.request("GET", "/v2/local/search/keyword.xml" + params, None, headers)
    res = conn.getresponse()

    libraryList = []

    if int(res.status) != 200:
        print("에러")
        conn.close()
        return libraryList

    libraryDoc = res.read().decode('utf-8')
    if libraryDoc == None:
        print("에러")
        conn.close()
        return libraryList

    parseData = parseString(libraryDoc)
    resultList = parseData.childNodes
    contentTypeList = resultList[0].childNodes
    for i in range(len(contentTypeList)-1):
        document = contentTypeList[i]
        library_ = Library()
        library_.setData(document.childNodes)
        libraryList.append(library_)
    conn.close()
    return libraryList


d = getBook("d_titl", "나미야 잡화점의 기적", 1)
for i in d:
    print(i.description)