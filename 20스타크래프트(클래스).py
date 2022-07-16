from random import *
#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) #self.name해도 상관없음 

    def move(self,location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]"\
            .format(self.name, location, self.speed))
    
    def damaged(self,damage): #메딕처럼 공격력이 없는 유닛도 데미지를 받을 수 있으니까
                              #어차피 하위클래스여서 상관없음 
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage 
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0: 
            print("{0} : 파괴되었습니다.".format(self.name))
#공격 유닛 
class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed)
        self.damage = damage 
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}"\
            .format(self.name, location, self.damage))

#마린, 매번 AttackUnit에 매개변수에 마린의 정보를 던져주는 것은 불편하니까
#마린은 AttackUnit에 속하니까 
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1 ,5)

#만약 def__init__(self, name, 40, 1 ,5) 하면 의미가 없으니까 
#고정 사용 목적이니까
#이전에는 def에서 매개변수에 할당된 값으로 정의를 했다면, 이번에는 직접 입력해서 정의한 것
#그리고 단순히 Marine클래스를 사용했을 때 attackunit이외에 다른 것은 필요가 없고 매개변수 필요한게 없으니
#self만 사용한것임 

    #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


#탱크

class Tank(AttackUnit):

    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동불가.
    seize_developed = False #시즈모드 개발여부
                            #tank1,2,3,4.. 개발함과 동시에 모두 적용이니까 
                            #init에 안하고 그 위에 함 
                            #init에 하면 새로 탱크를 만들때 마다 init이 실행되어 새로나온 unit은 false가 되니까
                            #근데 앞에다가 선언을 하면 tank클래스를 사용하는 모든 객체에 적용이 되는 거니까
                            #그리고 이렇게 밖에다 선언한 변수는 클래스이름.~ 으로 사용한다.
            

    def __init__(self): #init함수는 클래스를 호출할 때 사용되는 함수 
                        #다른 함수들은 내가 따로 호출을 해야함.
        AttackUnit.__init__(self, "탱크", 150, 1 , 35)
        self.seize_mode = False

    #init을 제외한 함수의 매개변수가 self로 시작하기 때문에 함수를 호출할 때 self.함수 이런식인 거임 
    #그리고 이때 self는 객체이름임 
    #wraith1 = FlyableAttackUnit(...)
    #wraith2 = FlyableAttackUnit(...)
    #wraith1, 2여도 이들의 이름은 wraith여야함.
    #wraith1 = FlyableAttackUnit("wraith"..)
    #...
    #self.name = name = wraith
    #따라서 wraith1.name 해도 wraith가 나오는 거임 
    #상위클래스를 호출하면 상위클래스의 init 하위클래스의 init 코드가 다 실행된다고 생각.
    #상위클래스에서 하위클래스의 함수를 부를 수 있는 것은 당연한것, 클래스를 떠나서 앞에 함수 주르륵 선언하고 함수내부에서 함수 호출 가능

    def set_seize_mode(self):
        if Tank.seize_developed == False: #def함수 밖에서 선언한 클래스 내에서 전역변수 느낌이니까 Tank
            return #객체 생성이후 self.set_seize_mode를 했는데 False면 return
                   #return을 만나면 이후 함수코드는 실행되지 않는다. 그리고 여기서는 리턴값이 없으니 아무것도 실행 안됨

        #현재 시즈모드가 아닐때 -> 시즈모드
        if self.seize_mode == False :
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


#날 수 있는 기능을 가진 클래스 

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed 

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날라갑니다. [속도{2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스 : 공격 유닛 + 날 수 있는 유닛 

class FlyableAttackUnit(AttackUnit, Flyable): 
    def __init__(self, name, hp, damage, flying_speed):  
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move1(self , location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#레이스

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제상태)
    
    def clocking(self):
        if self.clocked == True: #클로킹 모드 ->모드 해제
            print("{0} : 클로킹 모드 해제합니다.". format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.". format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg") #good gmae
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

#실제 게임 진행
game_start()

#마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 2기 생성

t1 = Tank()
t2 = Tank()

#레이스 1기 생성
w1 = Wraith()

#유닛 일괄 관리 (생성된 모든 유닛 append처리)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동 
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발 
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): #현재 객체가 클래스 Marine의 인스턴스냐(Marine클래스로 부터 나온 객체냐?)
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음

#게임종료
game_over()