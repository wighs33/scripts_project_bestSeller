from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
import webbrowser
import random

def getImage(url):      # url로 해당 이미지 생성
    if url == '':   # image가 없는 책의 경우
        img = loadImage('no_image.png', 90, 130) # 이미지 없음 image
        return img
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    img = Image.open(BytesIO(raw_data))
    img = img.resize((90, 130))   # image 크기 조정
    img = ImageTk.PhotoImage(img)
    return img
def getImage_Big(url):      # url로 해당 이미지 생성
    if url == '':   # image가 없는 책의 경우
        img = loadImage('no_image.png', 150, 197)  # 이미지 없음 image
        return img
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    img = Image.open(BytesIO(raw_data))
    img = img.resize((150, 197))   # image 크기 조정
    img = ImageTk.PhotoImage(img)
    return img
def loadImage(filename, w, h=0):    # menu에 쓰이는 이미지들 불러오기 및 크기 조정
    img = Image.open('res/'+filename)
    if h == 0:
        h = w
    img = img.resize((w, h))
    img = ImageTk.PhotoImage(img)
    return img
def changeTitle(title):     # 책 제목 라벨 크기에 맞게 변경
    c_title = ''
    line = 1
    over = False
    while len(title) > 7:
        if line == 3:
            over = True
            c_title += title[:5]
            c_title += '...'
            break
        else:
            c_title += title[:7]
            c_title += '\n'
            title = title[7:]
            line += 1
    if over is False:
        c_title += title
    return c_title
def changeText(text):     # 책 상세정보에서 제목, 저자 크키에 맞게 변경 / 첫번째 줄은 14자 그 뒤부터는 한줄에 17자
    c_text = ''
    if len(text) > 14:
        c_text += text[:14]
        c_text += '\n'
        text = text[14:]
        i = 0
        while len(text) > 17:
            if i == 2:
                c_text += text[:14]
                c_text += '...'
                return c_text
            c_text += text[:17]
            c_text += '\n'
            text = text[17:]
            i += 1
    c_text += text
    return c_text
def changeText_long(text):     # 즐겨찾기에서 제목, 저자 크키에 맞게 변경 / 첫번째 줄은 22자 그 뒤부터는 한줄에 25자
    c_text = ''
    l = 22
    if len(text) > l:
        c_text += text[:l]
        c_text += '\n'
        text = text[l:]
        while len(text) > l+3:
            c_text += text[:l+3]
            c_text += '\n'
            text = text[l+3:]
    c_text += text
    return c_text
def changeDescription(text):     # 책 상세정보에서 줄거리 크키에 맞게 줄넘김
    c_text = ''
    l = 29
    while len(text) > l:
        c_text += text[:l]
        c_text += '\n'
        text = text[l:]
    c_text += text
    return c_text
def changeLink(url):     # 책 상세정보에서 링크 크키에 맞게 줄넘김
    c_url = ''
    l = 48
    while len(url) > l:
        c_url += url[:l]
        c_url += '\n'
        url = url[l:]
    c_url += url
    return c_url
def changeDate(date):   # 출간일 형식 YYYY/MM/DD 로 변경
    c_date = ''
    c_date += date[:4]
    c_date += '/'
    date = date[4:]
    c_date += date[:2]
    c_date += '/'
    date = date[2:]
    c_date += date
    return c_date
def callback(url):  # 하이퍼링크
    webbrowser.open_new(url)
def random_color():     # 랜덤한 색상값 반환
    color = '#'
    colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(6):
        color += colors[random.randint(0, 15)]
    return color
def pubYear(pubdate):  # 출간 연도 반환
    return pubdate[:4]