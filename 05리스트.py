#리스트 : 순서를 가지는 객체의 집합 

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20 ,30] #순서를 가지게 변수를 한번에 묶음가능함 
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호")) #zero base

#리스트 함수 : append, insert, pop, count, sort, reverse, clear, extend
#append, insert, pop, sort, reverse, clear, extend 모두 기존변수값을 변경시킴 

#하하씨가 다음 정류장에서 다음칸에 탐 
subway.append("하하") #바로 뒤에 연이어 리스트 목록에 추가됨
print(subway) 

#정형돈씨를 유재석/ 조세호 사이에 태움
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명 있는지 확인 
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능 
num_list = [5,3,2,1,4]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형과 함께 사용가능
mix_list = ["조세호", 20 , True]

#리스트 확장
mix_list.extend(num_list)
print(mix_list)