sentence = "나는 소년입니다"
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
#큰따옴표 3개, 줄바꿈인식 여러줄 출력 
print(sentence3)

#슬라이싱 : 문자열에서 일부만 추출하고 싶은 경우 

jumin  = "981027-1234567"

print("성별 : " +jumin[7]) #이상, 미만, zero 베이스
print("연 : "+jumin[0:2]) # 0부터 2직전까지
print("월 : "+jumin[2:4])
print("일 :"+jumin[4:6])

print("생년월일 :"+jumin[0:6])
print("생년월일 :"+jumin[:6])
print("뒷자리: "+jumin[7:])
print("뒷자리: "+jumin[-7:]) # zero베이스 혹은 뒤에서부터 -1하면된다.

#문자열 함수(upper, lower, isupper, index, find, replace, count)
python = "Python is Amazing"
print(python.lower()) # 변수(문자열).함수
print(python.upper()) 
#lower, upper함수는 변수에 할당된 값을 변경하지 못한다 
print(python)
print(python[0].isupper())
#문자(문자열 슬라이싱).isupper() 해당 문자가 대문자면 True 반환 
print(len(python)) #공백 포함 문자 갯수 세기
print(python.replace("Python", "Java")) #변수에 할당된 값을 변경하지 못한다.
index = python.index("n") #python변수에 할당된 문자열 중 n 이라는 글자의 index를 반환 (zerobase)
print(index)
index = python.index("n",index +1) # ("글자", 시작위치) 앞에서 index변수에 할당된 값을 사용
print(index)

print(python.find("n")) 
print(python.find("Java")) #find("글자") 해당 글자가 있다면 index를 반환하고 없다면 -1을 반환한다.
#print(python.index("Java")) #index는 해당 글자가 없다면 오류를 내고 아래 구문들은 실행되지 못한다.
print(python.count("n"))

#문자열 포맷 
print("a" + "bcd") #abcd , 띄어쓰기 없음 
print("a", "b")

#방법1
print("나는 %d살입니다."%20) # (,)를 붙이지 않는다. c언어와 달리(,)를 붙이지 않고 %를 붙인다.
print("나는 %s를 좋아해요"%python)
print("Apple의 첫 글자는 %c입니다"%'A')

#정수, 문자열, 문자 모두 제어문자는 %s로 통일할 수 있다.
print("내 나이는 %s이고 %s색과 %s색을 좋아해요"%(20,'파란','빨강'))

#방법2 문자열.format()
print("나는 {}살이고 {}색과 {}색을 좋아합니다.".format(20,'파랑','빨강'))
print("나는 {0}살이고 {1}색과 {2}색을 좋아합니다.".format(20,'파랑','빨강'))
print("나는 {0}살이고 {2}색과 {1}색을 좋아합니다.".format(20,'파랑','빨강'))
#중괄호에 숫자가 없으면 차례로 들어가는것이고, 중괄호 안에 숫자가 있으면 그것이 index를 의미한다.

#방법3
print("나는{age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))
print("나는{color}살이며, {age}색을 좋아해요".format(age = 20, color = "빨간"))
#중괄호 안에 변수를 넣어 사용 가능함, 순서상관없이 호출한 변수가 들어감.
#동시에 안에서 선언,할당,호출이 모두 가능함. 안에서 선언한 변수는 밖에서 사용 불가함! 

#방법4, 외부에서 변수 선언한거 사용하고 싶은 경우 
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")


