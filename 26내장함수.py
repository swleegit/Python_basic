#내장함수 : 이미 내장되어 있어 따로 import가 필요없음

#ex) input

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

print(dir())
import random
print(dir())
import pickle
print(dir())

#random. 하면 뜨는 모듈안에 수많은 함수들을 확인하는 방법 
#import random한 상태에서
print(dir(random))

lst = [1,2,3]
print(dir(lst)) #리스트. 하면 나오는 수많은 함수들

name = "sungwoo"
print(dir(name)) #문자열. 하면 나오는 수많은 함수들  

#또는 구글에서 list of python builtins를 검색하면 
#파이썬 내장함수 나오고, 그 사용법이 나옴. 한국어 지원됨
#그래서 내가 필요한 기능이 있는지 확인해보자 