from tkinter import *
from tkinter import font
import tkinter.ttk
import func
import webbrowser
import book
from functools import partial

categoryDict = {'소설': 100, '시/에세이': 110, '경제/경영': 160, '자기계발': 170, '인문': 120, '역사/문화': 190, '가정/생활/요리': 130,
                '건강': 140, '취미/레저': 150, '사회': 180, '종교': 200, '예술/대중문화': 210, '학습/참고서': 220, '국어/외국어': 230,
                '사전': 240, '과학/공학': 250, '취업/수험서': 260, '여행/지도': 270, '컴퓨터/IT': 280, '잡지': 290, '청소년': 300, '유아': 310,
                '어린이': 320, '만화': 330, '해외도서': 340}
selected_color = 'yellow'   # 선택된 menu 버튼 색상
default_color = 'light grey'    # 선택되지 않은 menu 버튼 색상
myBooks = book.Book()
################################################################
# common
################################################################
def callback(url):  # 하이퍼링크
    webbrowser.open_new(url)
def openBook(books, index):     # 책 상세정보창 열기
    print(index)
    myBooks=books
    global new_myframe, new_canvas, b_menu
    for b in b_menu:
        b['state'] = 'disabled'
    new_myframe = Frame(window)
    new_myframe.place(x=20, y=30)
    scrollbar = Scrollbar(new_myframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    new_canvas = Canvas(new_myframe, bg='white', width=540, height=610, yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 700))
    new_canvas.pack()
    scrollbar.config(command=new_canvas.yview)

    image = func.getImage_Big(myBooks.images[index])
    info1 = '제목: '+func.changeTitleOfDetail(myBooks.titles[index])+'\n\n저자: '+func.changeText(myBooks.authors[index])+'\n\n출간일: '\
            +func.changeDate(myBooks.pubdates[index])+'\n\n가격: '+myBooks.prices[index]+'원'

    info2 = '줄거리\n\n'+func.changeDescription(myBooks.descriptions[index])

    info3 = '책 정보 링크\n'+func.changeLink(myBooks.links[index])

    font_ = font.Font(window, size=13, weight='normal', family='Consolas')
    l_bookImage = Label(new_canvas, image=image, width=150, height=203)
    l_bookImage.image = image  # 해줘야 이미지 뜸
    new_canvas.create_window(35, 30, anchor='nw', window=l_bookImage)

    l_bookInfo1 = Label(new_canvas, text=info1, font=font_, width=32, height=10, justify=LEFT)
    new_canvas.create_window(215, 30, anchor='nw', window=l_bookInfo1)

    l_bookInfo2 = Label(new_canvas, text=info2, font=font_, width=52, height=10, justify=LEFT)
    new_canvas.create_window(35, 250, anchor='nw', window=l_bookInfo2)

    l_bookInfo3 = Label(new_canvas, text=info3, font=font_, width=52, height=5, justify=LEFT, fg='blue', cursor='hand2')
    l_bookInfo3.bind('<Button-1>', lambda e: callback(myBooks.links[index]))
    new_canvas.create_window(35, 470, anchor='nw', window=l_bookInfo3)

    font_ = font.Font(window, size=30, weight='bold', family='Consolas')
    b_back = Button(new_canvas, text='◀', font=font_, command=closeBook, width=3, height=0)
    new_canvas.create_window(185, 585, anchor='nw', window=b_back)
    b_favorite = Button(new_canvas, text='☆', font=font_, command=addFavorites, width=3, height=0)
    new_canvas.create_window(295, 585, anchor='nw', window=b_favorite)
def closeBook():    # 책 상세정보창 닫기
    global new_myframe, new_canvas, b_menu
    for b in b_menu:
        b['state'] = 'normal'
    new_myframe.destroy()
    new_canvas.destroy()
def addFavorites():     # 책 즐겨찾기에 추가
    pass
def menuHome():
    global scene, b_menu
    if scene != 'home':     # home이 아닌 scene에서 home 버튼을 누르면 객체들 삭제 후 home 생성
        for obj in objects:
            obj.destroy()
        Init_Scene_Home()
        scene = 'home'
        for i in range(4):
            b_menu[i]['bg'] = default_color
        b_menu[0]['bg'] = selected_color
def menuSearch():
    global scene, b_menu
    if scene != 'search':     # search가 아닌 scene에서 search 버튼을 누르면 객체들 삭제 후 search 생성
        for obj in objects:
            obj.destroy()
        Init_Scene_Search()
        scene = 'search'
        for i in range(4):
            b_menu[i]['bg'] = default_color
        b_menu[1]['bg'] = selected_color
def menuFavorites():
    global scene, b_menu
    if scene != 'favorites':     # favorites가 아닌 scene에서 favorites 버튼을 누르면 객체들 삭제 후 favorites 생성
        for obj in objects:
            obj.destroy()
        Init_Scene_Favorites()
        scene = 'favorites'
        for i in range(4):
            b_menu[i]['bg'] = default_color
        b_menu[2]['bg'] = selected_color
def menuLibrary():
    global scene, b_menu
    if scene != 'library':     # library가 아닌 scene에서 library 버튼을 누르면 객체들 삭제 후 library 생성
        for obj in objects:
            obj.destroy()
        Init_Scene_Library()
        scene = 'library'
        for i in range(4):
            b_menu[i]['bg'] = default_color
        b_menu[3]['bg'] = selected_color
def Init_menuButton():
    global b_menu
    font_ = font.Font(window, size=20, weight='bold', family='Consolas')
    b_width, b_height = 10, 2
    b_x, b_y = 0, 662
    b_menu = []
    b_menu.append(Button(window, text="홈", bg=selected_color, command=menuHome, font=font_, width=b_width, height=b_height))
    b_menu.append(Button(window, text="검색", bg=default_color, command=menuSearch, font=font_, width=b_width, height=b_height))
    b_menu.append(Button(window, text="즐겨찾기", bg=default_color, command=menuFavorites, font=font_, width=b_width, height=b_height))
    b_menu.append(Button(window, text="도서관", bg=default_color, command=menuLibrary, font=font_, width=b_width, height=b_height))
    b_menu[0].place(x=b_x, y=b_y)
    b_menu[1].place(x=b_x+150, y=b_y)
    b_menu[2].place(x=b_x+300, y=b_y)
    b_menu[3].place(x=b_x+450, y=b_y)
################################################################
# home
################################################################
def Init_topLabel():
    font_ = font.Font(window, size=30, weight='bold', family='Consolas')
    topLabel = Label(window, text='Bestseller', font=font_)
    topLabel.place(x=185, y=20)

    objects.append(topLabel)
def Init_basic_bookList():
    myframe = Frame(window)
    myframe.place(x=20, y=100)
    scrollbar = Scrollbar(myframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas = Canvas(myframe, bg='white', width=540, height=540, yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 2050))
    canvas.pack()
    scrollbar.config(command=canvas.yview)

    # 나중에 데이터로 대체
    #################################
    y_distance = 290
    font_ = font.Font(window, size=17, weight='bold', family='Consolas')
    key = list(categoryDict.keys())
    for i in range(7):
        label = Label(canvas, text=key[i], font=font_, width=15)
        canvas.create_window(20, 15+y_distance*i, anchor='nw', window=label)

    books = []
    for i in range(7):
        tmpBook = book.Book()
        tmpBook.setData("d_catg", str(list(categoryDict.values())[i]), 4)
        books.append(tmpBook)

    imageList = []
    titleList = []

    font_ = font.Font(window, size=13, weight='normal', family='Consolas')
    for i in range(7):
        imageList.clear()
        titleList.clear()
        for url in books[i].images:
            imageList.append(func.getImage(url))
        for t in books[i].titles:
            titleList.append(func.changeTitle(t))
        for j in range(4):
            button = Button(canvas, image=imageList[j], command=partial(openBook, books[i], j), width=90, height=130)
            button.image = imageList[j]  # 해줘야 이미지 뜸
            canvas.create_window(30+130*j, 65+y_distance*i, anchor='nw', window=button)

            label = Label(canvas, text=titleList[j], font=font_, width=12, height=3)
            canvas.create_window(30-9+130*j, 210+y_distance*i, anchor='nw', window=label)

    objects.append(canvas)
    objects.append(myframe)
def Init_Scene_Home():
    Init_topLabel()
    Init_basic_bookList()
    Init_menuButton()
################################################################
# search
################################################################
def searchCategory():   # 분야별 검색
    global search_state, combobox, e_search
    if search_state != 'category':  # 저자, 제목 검색에서 분야 검색으로 전환하는 경우 - entry 삭제 후 combobox 생성
        e_search.destroy()
        objects.remove(e_search)
        Init_Combobox()
    search_state = 'category'
def searchAuthor():     # 저자별 검색
    global search_state, combobox, e_search
    if search_state == 'category':  # 분야 검색에서 저자 검색으로 전환하는 경우 - combobox 삭제 후 entry 생성
        combobox.destroy()
        objects.remove(combobox)
    else:  # 저자 검색에서 저자 or 제목 버튼 클릭 -> entry 초기화
        e_search.destroy()
        objects.remove(e_search)
    search_state = 'author'
    Init_searchEntry()
def searchTitle():      # 제목 검색
    global search_state, combobox, e_search
    if search_state == 'category':  # 분야 검색에서 제목 검색으로 전환하는 경우 - combobox 삭제 후 entry 생성
        combobox.destroy()
        objects.remove(combobox)
    else:  # 제목 검색에서 제목 or 저자 버튼 클릭 -> entry 초기화
        e_search.destroy()
        objects.remove(e_search)
    search_state = 'title'
    Init_searchEntry()
def Init_Combobox():
    global combobox
    font_ = font.Font(window, size=15, weight='bold', family='Consolas')
    lst = []
    for k in categoryDict.keys():
        lst.append(k)
    combobox = tkinter.ttk.Combobox(window, width=30, font=font_, values=lst)  # value=분야 리스트
    combobox.pack()
    combobox.place(x=80, y=150)
    combobox.set('분야 선택')  # combobox 텍스트 디폴트 값
    window.option_add('*TCombobox*Listbox.font', font_)  # combobox에 font 적용

    objects.append(combobox)
def Init_searchEntry():
    global e_search, search_state
    font_ = font.Font(window, size=15, weight='bold', family='Consolas')
    key = StringVar()
    key.set('저자명 입력') if search_state == 'author' else key.set('제목 입력')     # entry 텍스트 디폴트 값
    e_search = Entry(window, textvariable=key, justify=LEFT, font=font_)
    e_search.pack()
    e_search.place(x=80, y=150, width=350, height=30)

    objects.append(e_search)
def searchBook():
    global search_state
    if search_state == 'category':  # 검색 키워드 get
        keyword = combobox.get()
    else:
        keyword = e_search.get()
    print(keyword)
    if search_state == 'title':
        myBooks.setData("d_titl", keyword, 16)
    if search_state == 'category':
        myBooks.setData("d_catg", str(categoryDict[keyword]), 16)
    if search_state == 'author':
        myBooks.setData("d_auth", keyword, 16)
    showBookList()
def Init_threeButtons():
    font_ = font.Font(window, size=20, weight='bold', family='Consolas')
    b_width, b_height = 8, 2
    b_x, b_y = 55, 30
    b_category = Button(window, text="분야", command=searchCategory, font=font_, width=b_width, height=b_height)
    b_author = Button(window, text="저자", command=searchAuthor, font=font_, width=b_width, height=b_height)
    b_title = Button(window, text="제목", command=searchTitle, font=font_, width=b_width, height=b_height)
    b_category.place(x=b_x, y=b_y)
    b_author.place(x=b_x+180, y=b_y)
    b_title.place(x=b_x+360, y=b_y)

    objects.append(b_category)
    objects.append(b_author)
    objects.append(b_title)
def Init_searchKeyword():
    Init_Combobox()
    font_ = font.Font(window, size=15, weight='bold', family='Consolas')
    b_search = Button(window, text="검색", command=searchBook, font=font_, width=5)
    b_search.pack()
    b_search.place(x=450, y=144)

    objects.append(b_search)
def showBookList():
    myframe = Frame(window)
    myframe.pack()
    myframe.place(x=20, y=200)
    scrollbar = Scrollbar(myframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas = Canvas(myframe, bg='white', width=540, height=440, yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 900))
    canvas.pack()
    scrollbar.config(command=canvas.yview)

    imageList = []
    for url in myBooks.images:
        imageList.append(func.getImage(url))
    titleList = []
    for t in myBooks.titles:
        titleList.append(func.changeTitle(t))
    #################################
    y_distance = 220
    font_ = font.Font(window, size=13, weight='normal', family='Consolas')
    for i in range(myBooks.numberofbooks):
        button = Button(canvas, image=imageList[i], command=partial(openBook, myBooks, i), width=90, height=130)
        button.image = imageList[i]  # 해줘야 이미지 뜸
        canvas.create_window(30+130*(i%4), 15+y_distance*(i//4), anchor='nw', window=button)

        label = Label(canvas, text=titleList[i], font=font_, width=12, height=3)
        canvas.create_window(30-9+130*(i%4), 160+y_distance*(i//4), anchor='nw', window=label)

    objects.append(canvas)
    objects.append(myframe)
def Init_Scene_Search():
    global search_state
    search_state = 'category'   # 디폴트 - 분야별 검색
    Init_threeButtons()     # 분야, 저자, 제목 버튼 생성
    Init_searchKeyword()  # 검색 키워드 입력받는 combobox(분야) 또는 entry(저자,제목) 생성 & 검색 버튼 생성 / 디폴트 - 분야 검색
    showBookList()  # 검색에 따라 추천하는 책들 띄우기
################################################################
# favorites
################################################################
def Init_Scene_Favorites():
    pass
################################################################
# library
################################################################
def Init_Scene_Library():
    pass
window = Tk()
window.title('Bestseller')
window.geometry('600x750+450+30')
# myBooks.setData("d_titl", "인간", 16)

objects = []    # state 전환시 삭제될 객체들 보관

scene = 'home'  # 시작 scene = home
Init_Scene_Home()

window.mainloop()