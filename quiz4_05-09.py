'''
quiz)
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다 --

'''

#풀이 
from random import *
students = [i for i in range(1,21)]
shuffle(students)
chicken = sample(students, 1) #치킨 당첨자 한명 
#students.remove(chicken) #오류 발생함.
#sample로 리스트의 원소를 뽑는 것은 리스트 형식으로 뽑기 때문
#studnets리스트 원소에는 리스트 형식은 없고 정수형만 있기 때문

#오류발생하지 않으려면
students.remove(chicken[0]) #chicken = [어떤 숫자], chiecken[0] = 어떤 숫자

#치킨 당첨자를 제외한 19명 중 커피 3명 
coffee = sample(students,3)

#출력
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(chicken))
print("커피 당첨자 : {0}".format(coffee))
print("-- 축하합니다 --")

#해답
from random import *
students = list(range(1,21))
#print(type(range(1,21))) 그냥 range로만하면 타입은 range임, 리스트로 바꿀 필요가 있다.
shuffle(students)
winner = sample(students, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print("-- 축하합니다 --")




