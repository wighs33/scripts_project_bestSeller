from tkinter import *
from tkinter import font
import tkinter.ttk
import func

categoryDict = {'소설': 100, '시/에세이': 110, '경제/경영': 160, '자기계발': 170, '인문': 120, '역사/문화': 190, '가정/생활/요리': 130,
                '건강': 140, '취미/레저': 150, '사회': 180, '종교': 200, '예술/대중문화': 210, '학습/참고서': 220, '국어/외국어': 230,
                '사전': 240, '과학/공학': 250, '취업/수험서': 260, '여행/지도': 270, '컴퓨터/IT': 280, '잡지': 290, '청소년': 300, '유아': 310,
                '어린이': 320, '만화': 330, '해외도서': 340}
selected_color = 'yellow'   # 선택된 menu 버튼 색상
default_color = 'light grey'    # 선택되지 않은 menu 버튼 색상
################################################################
# home
################################################################
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
def Init_topLabel():
    font_ = font.Font(window, size=30, weight='bold', family='Consolas')
    topLabel = Label(window, text='Bestseller', font=font_)
    topLabel.place(x=185, y=20)

    objects.append(topLabel)
def Init_basicBooks():
    myframe = Frame(window)
    myframe.place(x=20, y=100)
    scrollbar = Scrollbar(myframe)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas = Canvas(myframe, bg='white', width=540, height=540, yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 2050))
    canvas.pack()
    scrollbar.config(command=canvas.yview)

    # 나중에 데이터로 대체
    #################################
    urlList = ['https://bookthumb-phinf.pstatic.net/cover/118/380/11838072.jpg?type=m1&amp;udate=20210322',
               'https://bookthumb-phinf.pstatic.net/cover/000/051/00005151.jpg?type=m1&amp;udate=20200416',
               'https://bookthumb-phinf.pstatic.net/cover/137/859/13785981.jpg?type=m1&amp;udate=20201104',
               'https://bookthumb-phinf.pstatic.net/cover/030/248/03024873.jpg?type=m1&amp;udate=20190831']
    imageList = []
    for url in urlList:
        imageList.append(func.getImage(url))

    tmp_titleList = ['편지', '11문자 살인사건', '브루투스의 심장 (완전범죄 살인릴레이)가나다라마', '마력의 태동 (라플라스의 탄생)']
    titleList = []
    for t in tmp_titleList:
        titleList.append(func.changeTitle(t))
    #################################

    y_distance = 290
    font_ = font.Font(window, size=17, weight='bold', family='Consolas')
    key = list(categoryDict.keys())
    for i in range(7):
        label = Label(canvas, text=key[i], font=font_, width=15)
        canvas.create_window(20, 15+y_distance*i, anchor='nw', window=label)

    font_ = font.Font(window, size=13, weight='normal', family='Consolas')
    for i in range(7):
        for j in range(4):
            button = Button(canvas, image=imageList[j], width=90, height=130)
            button.image = imageList[j]  # 해줘야 이미지 뜸
            canvas.create_window(30+130*j, 65+y_distance*i, anchor='nw', window=button)

            label = Label(canvas, text=titleList[j], font=font_, width=12, height=3)
            canvas.create_window(30-9+130*j, 210+y_distance*i, anchor='nw', window=label)

    objects.append(canvas)
    objects.append(myframe)
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
def Init_Scene_Home():
    Init_topLabel()
    Init_basicBooks()
    Init_menuButton()
################################################################
# search
################################################################
def searchCategory():   # 분야별 검색
    global search_state
    search_state = 'category'
def searchAuthor():     # 저자별 검색
    global search_state
    search_state = 'author'
def searchTitle():      # 제목 검색
    global search_state
    search_state = 'title'
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
def searchBook():
    pass
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
def Init_Scene_Search():
    global search_state
    search_state = 'category'   # 디폴트 - 분야별 검색
    Init_threeButtons()     # 분야, 저자, 제목 버튼 생성
    Init_searchKeyword()  # 검색 키워드 입력받는 combobox(분야) 또는 entry(저자,제목) 생성 & 검색 버튼 생성 / 디폴트 - 분야 검색
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

objects = []    # state 전환시 삭제될 객체들 보관

scene = 'home'  # 시작 scene = home
Init_Scene_Home()

window.mainloop()