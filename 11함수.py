#함수선언: 반복되는 코드는 함수로 만들어 편리하게 사용하자

#매개변수가 없는 경우 
def open_account():
    print("새로운 계좌가 형성되었습니다")

open_account() 
#def 함수이름(매개변수):
    #코드 작성
#함수이름(매개변수)  # 함수호출, 리턴값이 있다면 받을 변수가 있어야 활용가능함

#매개변수와 리턴값이 있는 경우

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은{0}원입니다.".format(balance + money))
    return balance + money

balance = 1000
balance = deposit(balance, 50000)
print(balance)

#출금 
#출금액< 잔액 : 출금 가능함 , 남은 금액 잔액 - 출금액

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다."\
            .format(balance - money))
        return balance - money
    else:
        print("출금이 불가합니다. 잔액은 {0}원입니다".format(balance))
        return balance
balance = 50000
balance = withdraw(balance, 20000)

#return 값 여러개 

def withdraw_night(balance, money):
    commission = 100
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은{0}원입니다".format(balance-money-commission))
        return commission, balance-money-commission

balance = 1000000
balance, commission = withdraw_night(balance, 1000)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


def profile(name, age, main_lang):
    print("이름 : {0}\t나이: {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))#긴 코드는 역슬래쉬로 끊어 단순화 표현 가능하다.
#def 함수이름(매개변수1,매개변수2,...):
    #실행할 코드, 함수에서 선언한 변수(매개변수) 활용 가능

profile("유재석", 20, "파이썬")
#함수이름(매개변수1,매개변수2,...)
#name = "유재석", age = 20, main_lang = "파이썬"으로 함수 내부에서 변수할당됨, 함수 밖에서는 사용불가

#기본값
#같은 학교 같은 학년 같은 반 같은 수업 
#가끔 예외가 생기는 경우

def profile_basic(name, age = 17 , main_lang = "파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어:{2}".format(name,age,main_lang))

profile_basic("유재석")
profile_basic("김태호")
profile_basic("조세호", 20 , 'Java') #이건 대입되서 진행됨 

#키워드 값 
def profile_keyword(name, age, main_lang):
    print(name, age, main_lang)

profile_keyword(name = "유재석", main_lang = "python", age = 20)
#함수선언시 매개변수를 이용해서 순서에 맞지 않아도 올바르게 출력되도록 할 수 있음

#가변 인자
def profile_1(name, age, lang1, lang2, lang3, lang4):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4)
#print함수는 뒤에서 줄바꿈이 자동으로 일어나지만 ,end = ' '하면 줄바꿈을 하지 않고 한칸 띄우고 아래 print 구문을 연이어 출력
#긴 print구문 또는 의미덩어리로 나누고 싶지만 한줄에 출력해야하는 경우 이를 활용한다.

profile_1("유재석", 20, "python", "c", "c++", "c#")
profile_1("김태호", 30, "c", "c++", "", "")
#언어를 4개이상 사용할 수 있어도 매개변수의 수의 제한 때문에 더 입력할 수 없다.
#이럴 때 가변인자를 사용하여 함수를 정의한다.

def profile_vari(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language: #사용시 *을 붙이지 않는다.
        print(lang, end = " ") #print 구문은 자동 줄바꿈이 일어나며, 연이어 출력하고 싶다면 , end= " "을 반드시 고려
    print() #줄바꿈을 위함 

profile_vari("유재석", 20, "python", 20, "python", "c", "c++", "c#", "java")
profile_vari("김태호", 30, "c", "c++")

#전역변수와 지역변수

# gun = 10
# def checkpoint(soilders): 
#     gun = gun - soilders
#     print("[함수내]남은 총: {0}".format(gun))

# checkpoint(2)
#위 구문은 오류 발생함. 선언한 함수 내에서 변수를 호출하려면, 매개변수, 안에서 따로 선언한 것, global을 통한 전역변수 사용 3가지 방법 중 하나

gun = 10 #전역변수 전체적으로 사용가능함. 이를 함수내에서 이용하려면 global을 같이 사용해야함 
def checkpoint(soilders): 
    gun = 20 #여기서 gun은 지역변수 함수 내에서만 사용 가능함
    gun = gun - soilders
    print("[함수내]남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun)) #이때 gun은 전역변수 따라서 10
checkpoint(2) #함수호출, 지역변수 사용 18
print("전체 총: {0}".format(gun))# 10

gun = 10 
def checkpoint(soilders): 
    global gun #밖에 선언된 전역변수 global을 사용한다는 의미. 밖에 선언된 global의 값을 변경시킬 수 있음.
    gun = gun - soilders
    print("[함수내]남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun)) #10
checkpoint(2) #8
print("전체 총: {0}".format(gun))# 8, 전역변수를 사용했기 때문에 할당된 값을 변경시킴 

#함수를 통해 전역변수 할당값을 바꾸고 싶다면 global 보다는 return값으로 받는 것을 주로 선호한다.

def checkpoint_ret(gun, soilders):
    gun = gun - soilders #이때 gun도 당연히 지역변수, 함수 내에서 만 유효함.
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun #함수 호출한 곳에 그대로 gun 값을 가져다 놓는다고 생각.

print("전체 총: {0}".format(gun)) #8
gun = checkpoint(2) #리턴값 6을 전역변수 gun에 할당함 
print("전체 총: {0}".format(gun))# 6






