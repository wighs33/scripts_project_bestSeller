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