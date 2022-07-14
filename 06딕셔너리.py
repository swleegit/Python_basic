#딕셔너리 : 사전이 단어와 그 의미가 있는 것처럼 딕셔너리는 key와 value로 구성이 된다 
#key와value는 일대일 대응, 키와 다른 value가 대응될 수 없다. 
#key는 중복이 허용될 수 없다 

cabinet = {3 : "유재석", 100 : "김태호 "}
print(cabinet[3]) #cabinet[key] : key에 해당하는 value값을 출력
print(cabinet[100])

#key에 해당하는 value를 출력하는 다른 방법
print(cabinet.get(3))
print(cabinet.get(5)) #5라는 key는 없음. 오류발생이 아니라 None출력 
print(cabinet.get(5, "사용가능")) #None 대신 사용가능 출력
#print(cabinet[5]) #오류남 

#key가 있는지 없는지 확인 방법

print(3 in cabinet)
print(5 in cabinet)
#있으면 True, 없으면 False

cabinet = {"A-3": "유재석", "A-100" : "김태호 "}
print(cabinet["A-3"]) #KEY로는 문자열도 가능함, 단 따옴표 반드시 붙이자.
print(cabinet["A-100"])

#새 손님
print(cabinet)  #cabinet = {"A-3": "유재석", "A-100" : "김태호 "}
cabinet["A-3"] = "김종국" #이미 있던 키의 값을 대체함
cabinet["C-20"] = "조세호" #없는 키의 경우는 추가한다. 
print(cabinet)

#간 손님 
del cabinet["A-3"] 
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력 
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)
