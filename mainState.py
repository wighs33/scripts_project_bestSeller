from tkinter import *
from tkinter import font
import tkinter.messagebox
window = Tk()
window.geometry("600x750+450+30")
DataList = []
pixelVirtual = PhotoImage(width=1, height=1)

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family ='Consolas')
    MainText = Label(window, font=TempFont, text="BEST SELLER")
    MainText.pack()

def InitMenuButton():
    h=2
    w=5
    TempFont = font.Font(window, size=20, weight='bold', family ='Consolas')
    HomeButton = Button(window, font = TempFont, text="홈", command=SearchButtonAction, height=h, width=w)
    HomeButton.pack()
    HomeButton.place(x=0, y=0)
    SearchButton = Button(window, font = TempFont, text="검색", height=h, width=w, command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=150, y=0)
    FavoritesButton = Button(window, font = TempFont, text="즐겨찾기", height=0, width=0, command=SearchButtonAction)
    FavoritesButton.pack()
    FavoritesButton.place(x=300, y=650)
    LibraryButton = Button(window, font = TempFont, text="도서관", height=0, width=0, command=SearchButtonAction)
    LibraryButton.pack()
    LibraryButton.place(x=450, y=650)

def InitHomeState():
    scrollbar = Scrollbar(window)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    tmpButton = Button(window, text="도서관", image=pixelVirtual, height=100, width=150, compound="c", command=SearchButtonAction)
    tmpButton.pack()
    tmpButton.place(x=300, y=300)

def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)

    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "도서관")
    SearchListBox.insert(2, "모범음식점")
    SearchListBox.insert(3, "마트")
    SearchListBox.insert(4, "문화공간")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)

    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family ='Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief ='ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=105)

def InitSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family ='Consolas')
    SearchButton = Button(window, font = TempFont, text="검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)


def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)  # ?댁쟾 異쒕젰 ?띿뒪??紐⑤몢 ??젣
    iSearchIndex = SearchListBox.curselection()[0]  # 由ъ뒪?몃컯???몃뜳??媛?몄삤湲?
    if iSearchIndex == 0:  # ?꾩꽌愿
        SearchLibrary()
    elif iSearchIndex == 1:  # 紐⑤쾾?뚯떇
        pass#SearchGoodFoodService()
    elif iSearchIndex == 2:  # 留덉폆
        pass#SearchMarket()
    elif iSearchIndex == 3:
        pass#SearchCultural()

    RenderText.configure(state='disabled')


def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes

            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes

                    if subitems[3].firstChild.nodeValue == InputLabel.get():  # 援??대쫫??媛숈쓣 寃쎌슦
                        pass
                    elif subitems[5].firstChild.nodeValue == InputLabel.get():  # ???대쫫??媛숈쓣 寃쎌슦
                        pass
                    else:
                        continue

                    # ?곗씠???쎌엯 援ш컙. ?곕씫泥섍? ?놁쓣 ?뚯뿉??"-"???ｋ뒗??
                    if subitems[29].firstChild is not None:
                        tel = str(subitems[29].firstChild.nodeValue)
                        pass  # ?꾩떆
                        if tel[0] != '0':
                            tel = "02-" + tel
                            pass
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))

            for i in range(len(DataList)):
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "] ")
                RenderText.insert(INSERT, "시설명: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "주소: ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "전화번호: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n\n")


def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(window, size=10, family='Consolas')
    RenderText = Text(window, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')


InitTopText()
InitMenuButton()
InitHomeState()
# InitSearchListBox()
# InitInputLabel()
# InitSearchButton()
# InitRenderText()
window.mainloop()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()