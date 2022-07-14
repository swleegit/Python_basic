#집합(set)
#중복안됨, 순서 없음 

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 집합을 다르게 선언 set([리스트])

#교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java or python)
print(java | python)
print(java.union(python)) #순서 보장되지 않음. 

#차집합 (java할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python할 줄 아는 사람이 늘어남 (원소 추가)
python.add("김태호")
print(python)

#java를 잊었어요 (원소 제외)
java.remove("김태호")
print(java)
