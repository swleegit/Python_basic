
#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]"\
            .format(self.name, location, self.speed))
#공격 유닛 
class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed)
        self.damage = damage 
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}"\
            .format(self.name, location, self.damage))

    def damaged(self,damage):
        print("{o} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage 
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0: 
            print("{0} : 파괴되었습니다.".format(self.name))


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
        AttackUnit.__init__(self, name, hp, 0, damage) #지상speed 매개변수가 있으니 써야함. 지상이 아니라 공중이니 지상 이송속도 0
        Flyable.__init__(self, flying_speed)
    
    def move1(self , location):
        print("[공중 유닛 이동]")#부모클래스<Flyable>의 함수fly을 사용해야함.
        self.fly(self.name, location)
        #init 그 아래 init에서 실행된 모든 변수와 함수(self.)는 사용할 수 있다.


#자식클래스가 꼭 부모클래스 init의 매개변수를 전부다 가질 필요 없다.
#flow를 보면 클래스 <FlyableAttackUnit>을 사용할 때 매개변수 name, hp, damage, flying_speed에 값을 할당해야함
#그렇게 정의된 변수는 아래 클래스에서 사용된다.
#AttackUnit 클래스는 변수로 name, hp, speed, damage를 갖는데 speed는 자식클래스 호출시 정의되지 않음
#근데 지금은 공중유닛이니까 필요없음. 그래서 그냥 자체적으로 0 으로 지정함 
#즉 자식클래스에서 부모클래스 init의 매개변수를 모두다 정의할 필요는 없지만 안된것은 따로 기입하든 해야함.
#필요한 매개변수가 3개인데 2개면 정의하는 것은 안됨! 

#벌쳐 : 지상 유닛, 기동성이 좋음 
vulture = AttackUnit("벌쳐", 80, 10 , 20)

#배틀크루져 : 공중유닛, 체룍도 굉장히 좋음, 공격력도 강함 
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move1("9시")

#지상이면 move 공중이면 fly로 구분해서 생각하는게 귀찮음 

#연산자 오버로딩 

#부모클래스에서 정의한 method말고 자식 클래스에서 정의한 method를 쓰고 싶을 때
#method를 새롭게 정의해서 사용할 수 있다. 