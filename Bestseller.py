from tkinter import *
from tkinter import font
import tkinter.ttk
from functools import partial
import func
from openAPI import *
import gmail
import telegram
#import spam1

categoryDict = {'소설': 100, '시/에세이': 110, '경제/경영': 160, '자기계발': 170, '인문': 120, '역사/문화': 190, '가정/생활/요리': 130,
                '건강': 140, '취미/레저': 150, '사회': 180, '종교': 200, '예술/대중문화': 210, '학습/참고서': 220, '국어/외국어': 230,
                '사전': 240, '과학/공학': 250, '취업/수험서': 260, '여행/지도': 270, '컴퓨터/IT': 280, '잡지': 290, '청소년': 300, '유아': 310,
                '어린이': 320, '만화': 330, '해외도서': 340}

################################################################
# common
################################################################'
def openBook(book, favorite):     # 책 상세정보창 열기  / 즐겨찾기된 책을 열면 favorite = True 아니면 False
    global new_myframe, new_canvas, b_menu, scene, topLabel
    for b in b_menu:
        b['state'] = 'disabled'
    if scene == 'home':
        topLabel.destroy()
    new_myframe = Frame(window)
    new_myframe.place(x=20, y=30)
    scrollbar = Scrollbar(new_myframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    new_canvas = Canvas(new_myframe, bg='white', width=540, height=610, yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 720))
    new_canvas.pack()
    scrollbar.config(command=new_canvas.yview)

    # 책 이미지 라벨
    img = func.getImage_Big(book.image)

    font_ = font.Font(window, size=13, weight='normal', family='Consolas')
    l_bookImage = Label(new_canvas, image=img, bd=4, relief='ridge', width=150, height=197)
    l_bookImage.image = img  # 해줘야 이미지 뜸
    new_canvas.create_window(35, 30, anchor='nw', window=l_bookImage)

    # 책 상세정보 info1
    info1 = '제목: '+func.changeText(book.title)+'\n\n저자: '+func.changeText(book.author)+'\n\n출간일: '\
            +func.changeDate(book.pubdate)+'\n\n가격: '+book.price+'원'
    # c++연동 - spam1.changeDate()로 변경

    l_bookInfo1 = Label(new_canvas, text=info1, bg='white', bd=1, relief='ridge', font=font_, width=32, height=10, justify=LEFT, anchor='w')
    new_canvas.create_window(215, 30, anchor='nw', window=l_bookInfo1)

    # 책 상세정보 info2
    info2 = '\n줄거리\n\n'+func.changeDescription(book.description)

    l_bookInfo2 = Label(new_canvas, text=info2, bg='white', bd=1, relief='ridge', font=font_, width=52, height=12, justify=LEFT, anchor='n')
    new_canvas.create_window(35, 250, anchor='nw', window=l_bookInfo2)

    # 책 상세정보 info3
    info3 = '책 정보 링크\n'+func.changeLink(book.link)

    l_bookInfo3 = Label(new_canvas, text=info3, bg='white', bd=1, relief='ridge', font=font_, width=52, height=5, justify=LEFT, fg='blue', cursor='hand2')
    l_bookInfo3.bind('<Button-1>', lambda e: func.callback(book.link))
    new_canvas.create_window(35, 510, anchor='nw', window=l_bookInfo3)

    # 뒤로가기 버튼
    back_img = func.loadImage('back_color.png', 60)
    b_back = Button(new_canvas, image=back_img, bg='white', bd=1, activebackground='white', command=closeBook, width=80, height=80)
    b_back.image = back_img
    new_canvas.create_window(180, 625, anchor='nw', window=b_back)
    # 즐겨찾기 버튼
    if book.favorites:    # 즐겨찾기된 책
        favorites_img = func.loadImage('favorites_remove_color.png', 60)
        b_favorite = Button(new_canvas, image=favorites_img, bd=1, bg='white', activebackground='white', command=partial(removeFavorites, book), width=80, height=80)
        b_favorite.image = favorites_img
    else:                 # 즐겨찾기되지 않은 책
        favorites_img = func.loadImage('favorites_add_color.png', 60)
        b_favorite = Button(new_canvas, image=favorites_img, bd=1, bg='white', activebackground='white', command=partial(addFavorites, book), width=80, height=80)
        b_favorite.image = favorites_img
    new_canvas.create_window(290, 625, anchor='nw', window=b_favorite)
def closeBook():    # 책 상세정보창 닫기
    global new_myframe, new_canvas, b_menu, scene, topLabel
    for b in b_menu:
        b['state'] = 'normal'
    if scene == 'home':
        Init_topLabel()
    new_myframe.destroy()
    new_canvas.destroy()
def addFavorites(book):     # 책 즐겨찾기에 추가
    global favorite_bookList
    book.favorites = True
    favorite_bookList.append(book)
def removeFavorites(book):     # 책 즐겨찾기에서 삭제
    global favorite_bookList
    book.favorites = False
    favorite_bookList.remove(book)
# 하단 메뉴버튼 4개(홈, 검색, 즐겨찾기, 도서관)
def menuHome():         # 메뉴 중 홈버튼 클릭 시 호출
    global scene, b_menu, menuImageList
    if scene != 'home':     # home이 아닌 scene에서 home 버튼을 누르면 객체들 삭제 후 home 생성
        for obj in objects:
            obj.destroy()
        Init_Scene_Home()
        scene = 'home'
        for i in range(4):
            if i == 0:
                b_menu[i]['bg'] = selected_color_bg
                b_menu[i].configure(image=menuImageList[i][1])
                b_menu[i].image = menuImageList[i][1]
            else:
                b_menu[i]['bg'] = default_color_bg
                b_menu[i].configure(image=menuImageList[i][0])
                b_menu[i].image = menuImageList[i][0]

def menuSearch():       # 메뉴 중 검색버튼 클릭 시 호출
    global scene, b_menu, menuImageList
    if scene != 'search':     # search가 아닌 scene에서 search 버튼을 누르면 객체들 삭제 후 search 생성
        for obj in objects:
            obj.destroy()
        Init_Scene_Search()
        scene = 'search'
        for i in range(4):
            if i == 1:
                b_menu[i]['bg'] = selected_color_bg
                b_menu[i].configure(image=menuImageList[i][1])
                b_menu[i].image = menuImageList[i][1]
            else:
                b_menu[i]['bg'] = default_color_bg
                b_menu[i].configure(image=menuImageList[i][0])
                b_menu[i].image = menuImageList[i][0]
def menuFavorites():    # 메뉴 중 즐겨찾기버튼 클릭 시 호출
    global scene, b_menu, menuImageList
    if scene != 'favorites':     # favorites가 아닌 scene에서 favorites 버튼을 누르면 객체들 삭제 후 favorites 생성
        for obj in objects:
            obj.destroy()
        Init_Scene_Favorites()
        scene = 'favorites'
        for i in range(4):
            if i == 2:
                b_menu[i]['bg'] = selected_color_bg
                b_menu[i].configure(image=menuImageList[i][1])
                b_menu[i].image = menuImageList[i][1]
            else:
                b_menu[i]['bg'] = default_color_bg
                b_menu[i].configure(image=menuImageList[i][0])
                b_menu[i].image = menuImageList[i][0]
def menuLibrary():      # 메뉴 중 도서관버튼 클릭 시 호출
    global scene, b_menu, menuImageList
    if scene != 'library':     # library가 아닌 scene에서 library 버튼을 누르면 객체들 삭제 후 library 생성
        for obj in objects:
            obj.destroy()
        Init_Scene_Library()
        scene = 'library'
        for i in range(4):
            if i == 3:
                b_menu[i]['bg'] = selected_color_bg
                b_menu[i].configure(image=menuImageList[i][1])
                b_menu[i].image = menuImageList[i][1]
            else:
                b_menu[i]['bg'] = default_color_bg
                b_menu[i].configure(image=menuImageList[i][0])
                b_menu[i].image = menuImageList[i][0]
def Init_menuButton():      # 하단의 메뉴(홈,검색,즐겨찾기,도서관) 버튼 생성
    global b_menu, menuImageList
    font_ = font.Font(window, size=20, weight='bold', family='Consolas')
    b_width, b_height = 150, 82
    b_x, b_y = 0, 662
    b_menu = []

    image_ = [['home_color', 'home_white'], ['search_color', 'search_white'], ['favorites_color', 'favorites_white'], ['library_color', 'library_white']]
    menuImageList = [[] for i in range(4)]
    for i in range(4):
        for j in range(2):
            menuImageList[i].append(func.loadImage(image_[i][j]+'.png', 60))

    b_menu.append(Button(window, image=menuImageList[0][1], bg=selected_color_bg, activebackground='white', command=menuHome, width=b_width, height=b_height))
    b_menu[0].image = menuImageList[0][1]
    b_menu.append(Button(window, image=menuImageList[1][0], bg=default_color_bg, activebackground='white', command=menuSearch, width=b_width, height=b_height))
    b_menu[1].image = menuImageList[1][0]
    b_menu.append(Button(window, image=menuImageList[2][0], bg=default_color_bg, activebackground='white', command=menuFavorites, width=b_width, height=b_height))
    b_menu[2].image = menuImageList[2][0]
    b_menu.append(Button(window, image=menuImageList[3][0], bg=default_color_bg, activebackground='white', command=menuLibrary, width=b_width, height=b_height))
    b_menu[3].image = menuImageList[3][0]

    b_menu[0].place(x=b_x, y=b_y)
    b_menu[1].place(x=b_x+150, y=b_y)
    b_menu[2].place(x=b_x+300, y=b_y)
    b_menu[3].place(x=b_x+450, y=b_y)
################################################################
# home
################################################################
def set_basic_bookList():   # home에서 기본적으로 추천해줄 대표분야 7가지 책 리스트
    global basic_bookList
    for i in range(7):
        basic_bookList.append(getBook('d_catg', str(list(categoryDict.values())[i]), 4))
def Init_topLabel():
    global topLabel
    font_ = font.Font(window, size=30, weight='bold', family='Consolas')
    topLabel = Label(window, text=' B E S T S E L L E R ', bd=1, relief='ridge', bg=basic_color1, fg='white', font=font_)
    topLabel.place(x=65, y=22)

    objects.append(topLabel)
def Init_basic_bookList():
    global basic_bookList
    myframe = Frame(window)
    myframe.place(x=20, y=100)
    scrollbar = Scrollbar(myframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas = Canvas(myframe, bg='white', width=540, height=540, yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 2050))
    canvas.pack()
    scrollbar.config(command=canvas.yview)

    y_distance = 290    # 분야별 간격
    categoryList = list(categoryDict.keys())    # 분야 한글 리스트

    for i in range(7):
        # 분야 7가지 라벨
        font_ = font.Font(window, size=17, weight='bold', family='Consolas')    # 분야 라벨 폰트
        label = Label(canvas, text=categoryList[i], bg=basic_color1, fg='white', font=font_, width=15)
        canvas.create_window(20, 15 + y_distance * i, anchor='nw', window=label)

        font_ = font.Font(window, size=13, weight='normal', family='Consolas')  # 제목 라벨 폰트
        for j in range(4):  # 분야별 4권 책 이미지(버튼), 제목(라벨)
            # 분야별 책 이미지 버튼
            img = func.getImage(basic_bookList[i][j].image)
            button = Button(canvas, image=img, command=partial(openBook, basic_bookList[i][j], False), width=90, height=130)
            button.image = img  # 해줘야 이미지 뜸
            canvas.create_window(30+130*j, 65+y_distance*i, anchor='nw', window=button)
            # 분야별 책 제목
            label = Label(canvas, text=func.changeTitle(basic_bookList[i][j].title), bg='white', bd=1, relief='ridge', font=font_, width=12, height=3)
            canvas.create_window(30-8+130*j, 210+y_distance*i, anchor='nw', window=label)

    objects.append(canvas)
    objects.append(myframe)
def Init_Scene_Home():
    Init_topLabel()     # 상단의 프로그램명 생성
    Init_basic_bookList()   # 대표분야 7가지에 대한 추천 책 4권씩 생성
    Init_menuButton()   # 하단의 메뉴(홈,검색,즐겨찾기,도서관)버튼 생성
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
def Init_Combobox():    # 분야 검색에 쓰이는 콥보박스 생성
    global combobox
    font_ = font.Font(window, size=15, weight='bold', family='Consolas')
    lst = []
    for k in categoryDict.keys():
        lst.append(k)
    combobox = tkinter.ttk.Combobox(window, width=30, font=font_, values=lst)  # value=분야 리스트
    combobox.pack()
    combobox.place(x=90, y=150)
    combobox.set('분야 선택')  # combobox 텍스트 디폴트 값
    window.option_add('*TCombobox*Listbox.font', font_)  # combobox에 font 적용

    objects.append(combobox)
def Init_searchEntry():     # 저자, 제목 검색에 쓰이는 엔트리
    global e_search, search_state
    font_ = font.Font(window, size=15, weight='bold', family='Consolas')
    key = StringVar()
    key.set('저자명 입력') if search_state == 'author' else key.set('제목 입력')     # entry 텍스트 디폴트 값
    e_search = Entry(window, textvariable=key, justify=LEFT, font=font_)
    e_search.pack()
    e_search.place(x=90, y=150, width=350, height=30)

    objects.append(e_search)
def searchBook():   # 키워드값을 가지고 책 리스트를 만듬
    global search_state, book_Canvas
    # 검색버튼 클릭시 캔버스 지우고 다시 생성
    book_Canvas.destroy()
    Init_booklistFrame()

    if search_state == 'category':  # 검색 키워드 get
        keyword = combobox.get()
    else:
        keyword = e_search.get()
    # 최대 16권의 검색 결과를 갖는 북 리스트 생성
    if search_state == 'category':
        bookList = getBook("d_catg", str(categoryDict[keyword]), 16)
    elif search_state == 'author':
        bookList = getBook("d_auth", keyword, 16)
    elif search_state == 'title':
        bookList = getBook("d_titl", keyword, 16)
    showBookList(bookList)
def showBookList(bookList): # 최대 16권의 겸색 결과를 화면에 띄움
    global book_Canvas
    y_distance = 220
    font_ = font.Font(window, size=13, weight='normal', family='Consolas')
    i = 0

    for book in bookList:
        # 검색된 책 이미지 버튼
        img = func.getImage(book.image)
        button = Button(book_Canvas, image=img, command=partial(openBook, book, False), width=90, height=130)
        button.image = img  # 해줘야 이미지 뜸
        book_Canvas.create_window(30+130*(i%4), 15+y_distance*(i//4), anchor='nw', window=button)
        # 검색된 책 제목 라벨
        label = Label(book_Canvas, text=func.changeTitle(book.title), bg='white', bd=1, relief='ridge', font=font_, width=12, height=3)
        book_Canvas.create_window(30-9+130*(i%4), 160+y_distance*(i//4), anchor='nw', window=label)
        i += 1
def Init_threeButtons1():
    font_ = font.Font(window, size=20, weight='bold', family='Consolas')
    b_width, b_height = 8, 2
    b_x, b_y = 55, 30
    b_category = Button(window, text="분야", bg='white', fg=basic_color1, activebackground='white', activeforeground=basic_color1, command=searchCategory, font=font_, width=b_width, height=b_height)
    b_author = Button(window, text="저자", bg='white', fg=basic_color1, activebackground='white', activeforeground=basic_color1, command=searchAuthor, font=font_, width=b_width, height=b_height)
    b_title = Button(window, text="제목", bg='white', fg=basic_color1, activebackground='white', activeforeground=basic_color1, command=searchTitle, font=font_, width=b_width, height=b_height)
    b_category.place(x=b_x, y=b_y)
    b_author.place(x=b_x+180, y=b_y)
    b_title.place(x=b_x+360, y=b_y)

    objects.append(b_category)
    objects.append(b_author)
    objects.append(b_title)
def Init_searchKeyword():
    Init_Combobox()
    search_img = func.loadImage('search_color.png', 35)
    b_search = Button(window, image=search_img, bg='white', activebackground='white', command=searchBook, width=45, height=45)
    b_search.image = search_img
    b_search.pack()
    b_search.place(x=460, y=139)

    objects.append(b_search)
def Init_booklistFrame():
    global book_Canvas
    myframe = Frame(window)
    myframe.pack()
    myframe.place(x=20, y=200)
    scrollbar = Scrollbar(myframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    book_Canvas = Canvas(myframe, bg='white', width=540, height=440, yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 900))
    book_Canvas.pack()
    scrollbar.config(command=book_Canvas.yview)

    objects.append(book_Canvas)
    objects.append(myframe)
def Init_Scene_Search():
    global search_state
    search_state = 'category'   # 디폴트 - 분야별 검색
    Init_threeButtons1()     # 분야, 저자, 제목 버튼 생성
    Init_searchKeyword()  # 검색 키워드 입력받는 combobox(분야) 또는 entry(저자,제목) 생성 & 검색 버튼 생성 / 디폴트 - 분야 검색
    Init_booklistFrame()  # 검색에 따라 추천하는 책들 띄울 프레임 생성
################################################################
# favorites
################################################################
def Init_mailaddressEntry():    # 메일 받을 주소 입력하는 엔트리 생성
    global mail_myframe, mail_canvas, e_rAddr
    mail_myframe = Frame(window)
    mail_myframe.pack()
    mail_myframe.place(x=20, y=20)
    mail_canvas = Canvas(mail_myframe, bg='white', width=557, height=115)
    mail_canvas.pack()

    font_ = font.Font(window, size=15, weight='bold', family='Consolas')

    label = Label(mail_canvas, text='메일 주소 입력:', bg='white', font=font_, height=1)
    mail_canvas.create_window(15, 44, anchor='nw', window=label)

    key = StringVar()
    e_rAddr = Entry(mail_canvas, textvariable=key, font=font_, width=25)
    mail_canvas.create_window(180, 45, anchor='nw', window=e_rAddr)

    send_img = func.loadImage('send_color.png', 35)
    button = Button(mail_canvas, image=send_img, activebackground='white', command=send_Mail, bg='white', width=45, height=45)
    button.image = send_img
    mail_canvas.create_window(470, 32, anchor='nw', window=button)

    close_img = func.loadImage('close_white.png', 30)
    b_close = Button(mail_canvas, image=close_img, bg=basic_color1, activebackground=basic_color1, command=closeMail, width=30, height=30)
    b_close.image = close_img
    mail_canvas.create_window(525, 0, anchor='nw', window=b_close)

    objects.append(mail_myframe)
    objects.append(mail_canvas)
def send_Mail():    # 전송버튼 클릭 시 이메일 보내기, 창 닫기
    global mail_myframe, mail_canvas, e_rAddr
    gmail.sendMail(favorite_bookList, e_rAddr.get())
    mail_myframe.destroy()
    mail_canvas.destroy()
def closeMail():    # 메일 주소 입력창 닫기
    global mail_myframe, mail_canvas
    mail_myframe.destroy()
    mail_canvas.destroy()
def showGraph():    # 그래프 보여주기
    global graph_myframe, graph_canvas
    graph_myframe = Frame(window)
    graph_myframe.pack()
    graph_myframe.place(x=20, y=150)
    graph_canvas = Canvas(graph_myframe, bg='white', width=557, height=490)
    graph_canvas.pack()

    font_ = font.Font(window, size=16, weight='bold', family='Consolas')
    l_graph = Label(graph_canvas, bg='white', text='출간 연도별 차트', font=font_)
    l_graph.place(x=95, y=35)

    data = {}
    for b in favorite_bookList:
        year = func.pubYear(b.pubdate)
        if year not in data.keys():
            data[year] = 1
        else:
            data[year] += 1

    start = 0
    s = sum(data.values())
    x, y = 20, 100
    l = 330
    y_dist = 20
    i = 0
    font_ = font.Font(window, size=14, weight='normal', family='Consolas')
    for key, value in data.items():
        extent = value / s * 360
        color = func.random_color()
        graph_canvas.create_arc((x, y, x+l, y+l), fill=color, outline='white', start=start, extent=extent)
        start = start + extent
        graph_canvas.create_rectangle(x+l+25, y+20*i+y_dist*i, x+l+25+20, y+20*(i+1)+y_dist*i, fill=color)
        label = Label(graph_canvas, text=key+'년도 - '+str(value)+'권', bg='white', font=font_)
        label.place(x=x+l+55, y=y+20*i+y_dist*i-4)
        i += 1

    close_img = func.loadImage('close_white.png', 45)
    b_close = Button(graph_canvas, image=close_img, bg=basic_color1, activebackground=basic_color1, command=closeGraph, width=45, height=45)
    b_close.image = close_img
    graph_canvas.create_window(510, 0, anchor='nw', window=b_close)

    objects.append(graph_myframe)
    objects.append(graph_canvas)
def closeGraph():   # 그래프 닫기
    global graph_myframe, graph_canvas
    graph_myframe.destroy()
    graph_canvas.destroy()
def Init_threeButtons2():
    font_ = font.Font(window, size=20, weight='bold', family='Consolas')
    b_width, b_height = 100, 100
    b_x, b_y = 157, 23

    mail_img = func.loadImage('mail_color.png', 80)
    b_mail = Button(window, image=mail_img, bg='white', activebackground='white', command=Init_mailaddressEntry, width=b_width, height=b_height)
    b_mail.image = mail_img

    graph_img = func.loadImage('graph_color.png', 80)
    b_graph = Button(window, image=graph_img, bg='white', activebackground='white', command=showGraph, font=font_, width=b_width, height=b_height)
    b_graph.image = graph_img

    b_mail.place(x=b_x, y=b_y)
    b_graph.place(x=b_x+180, y=b_y)

    objects.append(b_mail)
    objects.append(b_graph)
def Init_favorite_bookList():
    myframe = Frame(window)
    myframe.pack()
    myframe.place(x=20, y=150)
    scrollbar = Scrollbar(myframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas = Canvas(myframe, bg='white', width=540, height=490, yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 2430))
    canvas.pack()
    scrollbar.config(command=canvas.yview)

    y_distance = 160
    for i in range(len(favorite_bookList)):     # 즐겨찾기된 책 이미지(버튼), info(라벨)
        # 책 이미지 버튼
        img = func.getImage(favorite_bookList[i].image)
        button = Button(canvas, image=img, command=partial(openBook, favorite_bookList[i], True), width=90, height=130)
        button.image = img  # 해줘야 이미지 뜸
        canvas.create_window(15, 20+y_distance*i, anchor='nw', window=button)

        font_ = font.Font(window, size=10, weight='normal', family='Consolas')
        l_bg = Label(canvas, font=font_, bg='white', bd=1, relief='ridge', width=58, height=10, anchor='w')
        canvas.create_window(120, 14+y_distance*i, anchor='nw', window=l_bg)

        # 책 info1
        font_ = font.Font(window, size=13, weight='normal', family='Consolas')  # 책 info1 라벨 폰트
        info1 = '제목: '+func.changeText_long(favorite_bookList[i].title)+'\n저자: '+func.changeText_long(favorite_bookList[i].author)
        l_bookInfo1 = Label(canvas, text=info1, font=font_, bg='white', width=44, height=5, anchor='w', justify=LEFT)
        canvas.create_window(125, 15+y_distance*i, anchor='nw', window=l_bookInfo1)
        # 책 info2
        font_ = font.Font(window, size=8, weight='normal', family='Consolas')  # 책 info2 라벨 폰트
        info2 = '책 정보 링크\n' + favorite_bookList[i].link
        l_bookInfo2 = Label(canvas, text=info2, font=font_, bg='white', width=66, height=3, anchor='w', justify=LEFT, fg='blue', cursor='hand2')
        l_bookInfo2.bind('<Button-1>', lambda e: func.callback(favorite_bookList[i].link))
        canvas.create_window(125, 115 + y_distance * i, anchor='nw', window=l_bookInfo2)

    objects.append(canvas)
    objects.append(myframe)
def Init_Scene_Favorites():
    Init_threeButtons2()  # 이메일, 텔레그램, 그래프 버튼 생성
    Init_favorite_bookList()  # 즐겨찾기 리스트에 있는 책들 띄울 프레임 생성
################################################################
# library
################################################################
def addressSearch():     # 주소엔트리, 검색버튼
    font_ = font.Font(window, size=15, weight='bold', family='Consolas')
    key = StringVar()
    key.set('주소 입력')
    addressEntry = Entry(window, textvariable=key, justify=LEFT, font=font_)
    addressEntry.pack()
    addressEntry.place(x=80, y=80, width=350, height=30)

    font_ = font.Font(window, size=15, weight='bold', family='Consolas')
    searchButton = Button(window, text="검색", command=showAddressList, font=font_, width=5)
    searchButton.pack()
    searchButton.place(x=450, y=74)

    objects.append(addressEntry)
    objects.append(searchButton)

def showAddressList():
    global addressCanvas
    myframe = Frame(window)
    myframe.pack()
    myframe.place(x=20, y=200)
    scrollbar = Scrollbar(myframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    addressCanvas = Canvas(myframe, bg='white', width=400, height=440, yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 900))
    addressCanvas.pack()
    scrollbar.config(command=addressCanvas.yview)

    objects.append(addressCanvas)
    objects.append(myframe)

def mapButton():
    font_ = font.Font(window, size=15, weight='bold', family='Consolas')
    searchButton = Button(window, text="검색", command=searchBook, font=font_, width=5)
    searchButton.pack()
    searchButton.place(x=450, y=74)

    objects.append(searchButton)
def Init_Scene_Library():
    addressSearch()
    showAddressList()

basic_color1 = '#2fecb3'
basic_color2 = '#2fd8b3'
basic_color3 = '#2FC4B2'
# #2fecb3    1번째
# #2fd8b3    2번째
# #2FC4B2    3번째

selected_color_bg = basic_color1   # 선택된 menu 버튼 색상
default_color_bg = 'white'    # 선택되지 않은 menu 버튼 색상
selected_color_fg = basic_color1

window = Tk()
window.title('Bestseller')
window.geometry('600x750+450+30')
window.configure(bg=basic_color1)

objects = []    # state 전환시 삭제될 객체들 보관
scene = 'home'  # 시작 scene = home
favorite_bookList = []  # 즐겨찾기 책 리스트

basic_bookList = []  # home에서 추천해줄 대표분야 7가지 책
set_basic_bookList()

favorite_bookList.append(basic_bookList[0][0])
favorite_bookList.append(basic_bookList[0][1])
favorite_bookList.append(basic_bookList[0][2])
Init_Scene_Home()

#telegram.activeTelegramBot()     # 프로그램 실행 시 텔레그램 봇 활성화 / 베스트셀러 봇 2021 텔레그램에 검색

window.mainloop()

