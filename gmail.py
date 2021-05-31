# -*- coding: cp949 -*-
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import func

def makeText(bookList):
    text = ''
    for i in range(len(bookList)):
        text += '<br><img src='+bookList[i].image+'/>'
        text += '<p><br>제목: '+bookList[i].title+'<br>'
        text += '<br>저자: '+bookList[i].author+'<br>'
        text += '<br>출간일: '+func.changeDate(bookList[i].pubdate)+'<br>'
        text += '<br>가격: '+bookList[i].price+'원<br>'
        text += '<br>줄거리: '+bookList[i].description+'<br>'
        text += '<br>링크(상세정보): '+bookList[i].link+'<br>'
        text += '</p><br><hr>'
    return text
def sendMail(bookList, rAddr):
    #global value
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"
    htmlText = '<html><header></header><body><h1><b>Bestseller</b></h1><hr>'+makeText(bookList)+'</body></html>'

    senderAddr = "bestseller802@gmail.com"     # 보내는 사람 email 주소.
    recipientAddr = rAddr   # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "Favorites"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    HtmlPart = MIMEText(htmlText, 'html', _charset='UTF-8')

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = smtplib.SMTP(host, port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, "best802seller!")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()