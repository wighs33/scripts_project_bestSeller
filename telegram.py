#!/usr/bin/python
# coding=utf-8

import telepot
from pprint import pprint
from datetime import date
import sys
import traceback
import http.client
import func
import openAPI

client_id = "F5hus3tIzimtuicU0AVm"
client_secret = "MeU8Z5bALM"

conn = http.client.HTTPSConnection("openapi.naver.com")

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

TOKEN = '1796280016:AAFg0GMajb6Lcr2Fx0tvbEFqlb7XydcW8PM'
bot = telepot.Bot(TOKEN)

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def replyBookData(user, catg_param):
    print(user, catg_param)
    bookList = openAPI.getBook('d_catg', catg_param, 10)    # 분야별 검색 / 분야코드 / 검색할 책 수(10개 고정)

    if len(bookList) == 0:
        sendMessage(user, '해당하는 데이터가 없습니다.')
    else:
        msg = ''
        i = 1
        for b in bookList:
            msg += '-----------------------------------------------------------------------------------------------------\n'
            msg += '     '+str(i)+'\n'
            msg += '-----------------------------------------------------------------------------------------------------\n'
            msg += '제목:  '+b.title+'\n\n'
            msg += '저자:  '+b.author+'\n\n'
            msg += '출간일:  '+func.changeDate(b.pubdate)+'\n\n'
            msg += '가격:  '+b.price+'원\n\n'
            msg += '줄거리\n'+b.description+'\n\n'
            msg += '링크(상세정보)\n'+b.link+'\n\n\n'

            sendMessage(user, msg)

            msg = ''
            i += 1

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('분야') and len(args) > 1:
        print('try to 분야', args[1])
        replyBookData(chat_id, args[1])
    else:
        sendMessage(chat_id, '모르는 명령어입니다.\n\n분야 중 하나를 선택해 분야코드를 입력하세요.\n분야 [분야코드]\nex) 분야 100, 분야 300\n\n분야코드\n'
                             '소설: 100, 시/에세이: 110, 경제/경영: 160, 자기계발: 170, 인문: 120, 역사/문화: 190, 가정/생활/요리: 130, '
                             '건강: 140, 취미/레저: 150, 사회: 180, 종교: 200, 예술/대중문화: 210, 학습/참고서: 220, 국어/외국어: 230, '
                             '사전: 240, 과학/공학: 250, 취업/수험서: 260, 여행/지도: 270, 컴퓨터/IT: 280, 잡지: 290, 청소년: 300, 유아: 310, '
                             '어린이: 320, 만화: 330, 해외도서: 340')

def activeTelegramBot():
    today = date.today()

    print('[', today, ']received token :', TOKEN)

    bot = telepot.Bot(TOKEN)
    pprint(bot.getMe())

    bot.message_loop(handle)

    print('Listening...')