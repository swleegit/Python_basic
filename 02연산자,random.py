#파일-기본설정-설정-terminal font 검색 - 크기 조정가능 
print(1+1)
print(5*2)
print(6/3)
print(2**3)
print(5%3) #나머지 구하기
print(10%3)
print(5//3) # 몫 구하기
print(5>=3)
print(5==3) # 같으면 True
print(5!=3) # 다르면 True
print(4 + 3 == 7) #계산순서 파악, 헷갈리면 ()를 붙여서 

print(not(3!=5)) #False
print((3>0) and (3<5)) #and 대신 & 사용 가능, 둘 중 어느하나 False
print((1>2) or (2<5)) #or 대신 | 사용 가능, 둘 중 어느하나가 True
print(3<4<5) # 참, c언어와 구분, c언어는 차례로 진행 참이면 1을 반환하고 그 수로 대소 비교함.

print(2 + 3 * 4) #연산순서는 수학에서와 같다
number = 2 + 3 * 4 
print(number)
number = number * 4 #64
number *= 4 #256
number %= 5 # 4
number /= 2 # 2
number -= 0.5 # 1.5
print(number)

#숫자 처리 함수

print(abs(-5))
print(pow(4,2)) #4의 제곱
print(max(5,2)) #최대값
print(min(5,3))
print(round(3.14))
print(round(4.9))

#모듈 사용 
from math import * #math 모듈에서 전부(*)를 가져옵니다.
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 3
print(sqrt(16)) # 16의 제곱근 4 
#floor, ceil, sqrt 함수들은 모듈에서 가져온것 

#랜덤함수 사용
from random import * 
print(random()) # 0.0~1.0미만의 임의의 값 생성
print(random() * 10) #0.0~ 10.0미만
print(int(random()*10)+1) #int()정수형 자료형으로 만들어줌
#1~10이하 정수 출력

#1~45의 숫자 7개를 뽑아보자.

#방법1 random()함수 이용

print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

#방법2 randrange
print(randrange(1,46)) #1이상 46미만 정수 랜덤
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))

#방법3 randint
print(randint(1,45)) #이상 이하, 정수
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))

