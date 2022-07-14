#튜플
#리스트와 딕셔너리와 다르게 내용 변경이나 추가를 할 수 없음 
#처리속도가 빠름 , 변경되지 않는 목록에 사용하기 편함

menu = ("돈까스" ,"치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")  : 튜플은 추가 기능 없음 

#name = "김종국"
#age = 20
#hobby = "코딩"
#print(name, age, hobby)
(name, age ,hobby) = ("김종국", 20 , "코딩")
name, age ,hobby = "김종국", 20 , "코딩"
print(name, age, hobby)