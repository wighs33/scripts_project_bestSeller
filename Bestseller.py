from tkinter import *
from tkinter import font

################################################################
# home
################################################################
def Init_topLabel():
    font_ = font.Font(window, size=30, weight='bold', family='Consolas')
    topLabel = Label(window, text='Bestseller', font=font_)
    topLabel.place(x=185, y=20)

def Init_HomeState():
    Init_topLabel()

window = Tk()
window.title('Bestseller')
window.geometry('600x750+450+30')

Init_HomeState()

window.mainloop()