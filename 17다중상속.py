#다중 상속
#부모클래스가 여러개, 즉 상속의 원천이 여러개인경우 

#일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

#공격 유닛 
class AttackUnit(Unit): 
    def __init__(self, name, hp, damage): 
        Unit.__init__(self, name, hp)
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

#드랍쉽 : 공중유닛, 수송기. 마린/파이어뱃/ 탱크 등을 수송. 공격x 

#날 수 있는 기능을 가진 클래스 

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed #이 Flyable은 작은 클래스로 어차피 같이 쓰는 거임.
                                         #이름에 대한 정보는 다른 클래스에 있어서 안쓴것 

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날라갑니다. [속도{2}]"\
            .format(name, location, self.flying_speed)) #자신의 클래스 안에서 선언된 멤버변수를 사용할 수 있다.

#공중 공격 유닛 클래스 : 공격 유닛 + 날 수 있는 유닛 

class FlyableAttackUnit(AttackUnit, Flyable): #작은 여러개의 클라스, 그걸 포괄하는 클래스, 덩어리 단위로 클래스를 만들자
    def __init__(self, name, hp, damage, flying_speed): #자식클래스의 init함수는 부모클래스의 매개변수를 모두 포함하고 있어야한다.
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
        #FlyableAttackUnit 클래스는 두개의 부모클래스를 합치는 용도로 사용됨 
        #부모의 init메서드 말고도 다른 메서드도 사용 가능함 

'''
FlyableAttackUnit 클래스 : AttackUnit, Flyable 클래스 내용을 상속받음
<FlyableAttackUnit> 
    
    <AttackUnit>
        <Unit>
            name
            hp
        damage
        attack(location)
        damaged(damage)

    <Flyable>
        flying_speed
        fly(name, location)

FlyableAttackUnit의 객체는 이 모든 기능을 사용할 수 있음
'''

#하나의 단위 역할을 하는 작은 클래스를 만든 다음 유닛의 능력에 따라 작은 클래스를 상속 받으면 됨 

#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사 

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
#이렇게 하면 FlyableAttackUnit의 init과 부모클래스에 속한 init이 모두 사용됨
#다른 메서드는 내가 따로 호출해야 실행됨! 

#flow를 적어보자면 
#FlyableAttackUnit클래스로 valkyrie(self)라는 객체를 만듬 
#이때 매개변수는 name, hp, damage, flying_speed로 부모클래스의 init함수의 매개변수를 모두 포함하고 있음
#해당코드는 자식클래스, 부모클래스의 init함수를 호출한다.
#name과 hp는 <AttackUnit>의 부모 클래스인<Unit>의 init에 따라 self.name = "발키리", self.hp = 200으로 정의된다.
#damage는 <AttackUnit>의 init에 따라 self.damage = 6으로 정의된다. 
#flying_speed는 <Flyable>의 init에 따라 self.flying_speed = 5로 정의된다.
#init함수만 사용되었으며 각 클래스의 추가함수를 위해서는 따로 호출해야한다.

valkyrie.fly(valkyrie.name, "3")
#자식 클래스<Flyable>에 fly함수를 호출한다.


