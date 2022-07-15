'''
quiz)
표준 체중을 구하는 프로그램을 작성하시오

*표준 체중 : 각 개인의 키에 적당한 체중 

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시 

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg입니다.
'''

#풀이1

def std_weight():
    while True:
        gender = input("성별(남자,여자)>>")
        height = float(input("키(cm)>>")) #숫자로 구성된 str이라면 바로 float진행해도된다.

        if gender == "남자":
            return height, gender, round((height*height*0.0001*22),2)
            break
        
        elif gender == "여자":
            return height, gender, round((height*height*0.0001*21),2)
            break
    
        else:
            print("잘못된 입력입니다 : 성별(남자, 여자), 키(cm)")

height, gender, weight = std_weight()
print("키{0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))

#해답 

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender), 2) #int형인데 / 하면 결과값은 float
print("키{0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))
