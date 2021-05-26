# import book
#
# b = book.Book()
# b.setData("d_titl", "사람", 16)
# print(b.titles)
# print(b.links)
# print(b.images)
# print(b.authors)
# print(b.prices)
# print(b.discounts)
# print(b.publishers)
# print(b.pubdates)
# print(b.isbns)
# print(b.descriptions)
# print(b.numberofbooks)

categoryDict = {'소설': 100, '시/에세이': 110, '경제/경영': 160, '자기계발': 170, '인문': 120, '역사/문화': 190, '가정/생활/요리': 130,
                '건강': 140, '취미/레저': 150, '사회': 180, '종교': 200, '예술/대중문화': 210, '학습/참고서': 220, '국어/외국어': 230,
                '사전': 240, '과학/공학': 250, '취업/수험서': 260, '여행/지도': 270, '컴퓨터/IT': 280, '잡지': 290, '청소년': 300, '유아': 310,
                '어린이': 320, '만화': 330, '해외도서': 340}


print(categoryDict['건강'])