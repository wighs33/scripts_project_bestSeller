from tkinter import *
from tkinter import font

################################################################
# home
################################################################
def menuHome():
    pass
def menuSearch():
    pass
def menuFavorites():
    pass
def menuLibrary():
    pass
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
def Init_menuButton():
    font_ = font.Font(window, size=20, weight='bold', family='Consolas')
    b_width, b_height = 10, 2
    b_x, b_y = 0, 662
    b_menu = []
    b_menu.append(Button(window, text="홈", command=menuHome, font=font_, width=b_width, height=b_height))
    b_menu.append(Button(window, text="검색", command=menuSearch, font=font_, width=b_width, height=b_height))
    b_menu.append(Button(window, text="즐겨찾기", command=menuFavorites, font=font_, width=b_width, height=b_height))
    b_menu.append(Button(window, text="도서관", command=menuLibrary, font=font_, width=b_width, height=b_height))
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

Init_HomeState()

window.mainloop()