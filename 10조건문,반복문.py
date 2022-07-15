#if, elif, else
weather = input("오늘 날씨 어떄요?") #사용자의 입력을 기다림, 입력이 weather변수에 할당됨, 입력값을 문자열로 할당함! 

if weather == "비" or weather == "눈":
    print("우산을 챙기세요")

elif weather == "미세먼지":
    print("마스크를 챙기세요")

else:
    print("준비물이 필요 없어요")

#조건문이 참이면 아래 실행(불 자료형이 와야함!)
#(:) 빼먹지 말고 
#and or을 활용할 생각하자.
#if elif elif.. else : short cut 

temp = int(input("기온은 어때요?"))
#input 문자열을 정수형으로 변환 

if 30 <= temp:
    print("너무 더워요 나가지마세요.")

elif temp >= 10 and temp <= 30:
    print("괜찮은 날씨에요")

elif 0 <= temp < 10:  # 범위 표현 방법 2가지 
    print("외투를 챙기세요")

else:
    print("너무 추워요, 나가지마세요")

#for 반복문

for waiting_no in [1,2,3,4,5]:
    print("대기번호: {0}".format(waiting_no))
#리스트 원소들이 차례로 waiting_no라는 변수에 대입이 되고, 아래 반복문을 실행하고 끝나면 다시 다음 차례
#특정 원소로 할경우 리스트를 활용해도 ok

#순차적으로 커지는 수 활용 range()활용하자 
for waiting_no in range(5): #0,1,2,3,4
    print("대기번호: {0}".format(waiting_no))

for waiting_no in range(1,6): #1,2,3,4,5
    print("대기번호: {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))

#while
customer = "토르"
index = 5 
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
    index -= 1 # 반복마다 깎을 때
    if index == 0: #어느 일정 수준 도달 했을 때 
        print("커피는 폐기 처분 되었어요.")

customer = "아이언맨"
index = 1 # while에서 몇번 반복되었는지 맞추기 위해

# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출{1}회".format(customer, index))
#     index += 1 #회수 카운팅 
    #무한반복문을 나오기 위해서 cntrl ^c 
    #여기에 타이핑이 안되는 이유는 while 무한 반복인데 나올 수 있는 코드가 없어서임.

customer = "토르"
person = "Unknown"

while person != customer: #person이 토르가 될 때까지 무한반복이니까 토르와 person이 달라야 물어보는걸 계속함
    print("{0}, 커피가 준비되었습니다".format(customer))
    person = input("이름이 어떻게 되세요?")
#반복문(for, while), 조건문(if, elif, else)에서 변수는 전역변수 그대로 사용가능함
#함수에서 전역변수를 사용하려면 global 해야함.

#continue와 break
absent = [2,5]
no_book = [7]
for student in range(1, 11):
    if student in absent: #원소 in 리스트 : 원소가 리스트안에 있나요?
        continue #현재 반복을 끊고 다음 반복으로 넘어감

    elif student in no_book:
        print("오늘 수업은 여기까지. {0}교무실로 따라와".format(student))
        break #현재 반복문을 바로나옴

    #결석과 책이 없는 것은 동시에 일어날 수 없음. 코드의 효율을 위해서 if elif 구문을 사용함
    #들여쓰기로 되어 있는것이 코드에 속하는 것 
    print("{0}, 책을 읽어봐요".format(student))
    #반복문에 print 구문 속해있으니 break 만나면 위의 코드도 실행되지 않는다.

#한줄 for : 리스트와의 활용

#1
students = [1,2,3,4,5]
print(students)
students = [i +100 for i in students]
print(students)

#2
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

#3
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
#students의 원소를 차례로 i에 대입, i는 문자열, 문자열.upper(): 모두 대문자로 반환, 그것이 새로운 원소
#이를 차례로 진행해서 새로운 원소를 만든다.

