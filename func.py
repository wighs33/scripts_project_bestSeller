from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk


def getImage(url):      # url로 해당 이미지 생성
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image


def changeTitle(title):     # 책 제목 라벨 크키에 맞게 변경
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