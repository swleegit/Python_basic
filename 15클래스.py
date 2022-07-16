#마린 : 공격 유닛, 군인. 총을 쏠 수 있음 
name = "마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다".format(name))
print("체력 : {0}, 공격력 : {1}\n".format(hp, damage))

#탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반/시즈 모드

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다".format(tank_name))
print("체력 : {0}, 공격력 : {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다".format(tank2_name))
print("체력 : {0}, 공격력 : {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]".\
        format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

#탱크 한마리더 추가 
#유닛은 수십 수백마리 그 때 마다 변수를 새롭게 정의하는 일은 매우 귀찮은 일 
#이러한 경우 클래스가 유용하다

#클래스
#붕어빵기계 : 어떠한 틀임 거기에 재료만 넣으면 붕어빵은 무한정 만들어 낼 수 있음.
#반복되는 형식을 어떠한 틀(클래스)을 만들어 반복되는 형식에 대해 효율을 높인다.
#서로 연관이 있는 변수와 함수의 집합 

class Unit: #class 클래스이름(대문자로 시작, 캐멀케이스)
    def __init__(self, name, hp, damage): #__init__ 객체가 만들어질 때 자동으로 호출되는 부분 
        self.name = name #init의 첫번째 변수.변수이름 = 할당값, 멤버변수에 값을 할당하는 과정
                         #여기서는 클래스가 받은 매개변수 name의 값을 할당
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name)) #Unit 클래스를 호출하면 init함수가 호출되면서 해당 코드가 실행됨 
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#__init__
#파이썬에서 사용되는 생성자
#마린이나 탱크같은 객체가 만들어 질때 자동으로 호출되는 부분
#객체 : 마린과 탱크와 같이 클래스로부터 만들어지는 것들
#이때 마린과 탱크는 Unit 클래스의 인스턴스라고 한다. 
#객체가 생성될 때는 init함수의 매개변수(self제외)수 만큼 값을 지정해야한다.

#멤버 변수  
#클래스 내에서 정의된 변수
#self.변수이름 이런 형태
#이 변수를 클래스 내에서 사용 가능하다.
 
#멤버 변수를 클래스 외부에서 사용하는 방법 
#레이스 : 공중유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#클래스를 이용해서 만든 객체에 한해 사용가능함.
#객체.멤버변수 이런형태로 사용가능함.

#클래스를 활용한 코드의 flow를 확인해보자
wraith1 = Unit("레이스", 80, 5)
#Unit클래스(틀)을 호출-> 클래스 선언 부분으로 이동함 
#__init__함수가 호출됨, name에는 "레이스", hp에는 80, damage에는 5를 할당함.
#그것이 클래스 안에 있는 멤버변수인 self.~에 차례로 할당됨
#__init__함수 코드인 print 구문 내용이 출력됨 
#여기까지보면 클래스나 함수나 같은거 아니냐 싶겠지만 
#wraith1이라는 객체가 형성됨. 이 객체는 자체로 name, hp, damage 정보를 가지고 있음.
#따라서 wraith1.name ="레이스", wraith1.hp = 80, wraith.damage = 5 라는 변수(객체정보) 활용 가능함

'''
--wraith1--
name : wratih
hp : 80
damage = 5
'''
