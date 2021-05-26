from tkinter import *
from tkinter import font
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
    if scene != 'home':
        scene = 'home'
        for i in range(4):
            b_menu[i]['bg'] = default_color
        b_menu[0]['bg'] = selected_color
def menuSearch():
    global scene, b_menu
    if scene != 'search':
        scene = 'search'
        for i in range(4):
            b_menu[i]['bg'] = default_color
        b_menu[1]['bg'] = selected_color
def menuFavorites():
    global scene, b_menu
    if scene != 'favorites':
        scene = 'favorites'
        for i in range(4):
            b_menu[i]['bg'] = default_color
        b_menu[2]['bg'] = selected_color
def menuLibrary():
    global scene, b_menu
    if scene != 'library':
        scene = 'library'
        for i in range(4):
            b_menu[i]['bg'] = default_color
        b_menu[3]['bg'] = selected_color
def Init_topLabel():
    font_ = font.Font(window, size=30, weight='bold', family='Consolas')
    topLabel = Label(window, text='Bestseller', font=font_)
    topLabel.place(x=185, y=20)
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
def Init_HomeState():
    Init_topLabel()
    Init_basicBooks()
    Init_menuButton()

window = Tk()
window.title('Bestseller')
window.geometry('600x750+450+30')

scene = 'home'  # 시작 scene = home
Init_HomeState()

window.mainloop()