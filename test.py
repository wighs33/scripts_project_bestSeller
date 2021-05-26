# -*- coding:cp949 -*-
import os
import sys
import urllib.request
from xml.dom.minidom import parseString

client_id = "F5hus3tIzimtuicU0AVm"
client_secret = "MeU8Z5bALM"
encText = urllib.parse.quote("위즈덤하우스")
url = "https://openapi.naver.com/v1/search/book_adv.xml?d_publ="+encText
resp = None

req = urllib.request.Request(url)
req.add_header("X-Naver-Client-Id",client_id)
req.add_header("X-Naver-Client-Secret",client_secret)
try:
    resp = urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)
    print(parseString(e.read().decode('utf-8')).toprettyxml())
except urllib.error.HTTPError as e:
    print("error code=" + e.code)
    print(parseString(e.read().decode('utf-8')).toprettyxml())
else:
    response_body = resp.read()
    print(parseString(response_body.decode('utf-8')).toprettyxml())




