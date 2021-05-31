from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
import webbrowser

def getImage(url):      # url로 해당 이미지 생성
    if url == '':   # image가 없는 책의 경우
        url = 'https://img.icons8.com/ios/452/no-image.png' # 이미지 없음 image
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((90, 130))   # image 크기 조정
    image = ImageTk.PhotoImage(im)
    return image
def getImage_Big(url):      # url로 해당 이미지 생성
    if url == '':   # image가 없는 책의 경우
        url = 'https://img.icons8.com/ios/452/no-image.png' # 이미지 없음 image
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((150, 203))   # image 크기 조정
    image = ImageTk.PhotoImage(im)
    return image
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
        while len(text) > 17:
            c_text += text[:17]
            c_text += '\n'
            text = text[17:]
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
def pubYear(pubdate):  # 출간 연도 반환
    return pubdate[:4]