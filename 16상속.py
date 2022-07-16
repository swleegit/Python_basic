#상속
#class의 내용을 보니까 AttackUnit의 클래스와 비슷한 점이 많음 
#이럴때 상속가능함, 상속은 물려받는 것을 의미한다. Unit 클래스의 내용을 상속받아서 AttackUnit을 만든다
#큰 클라스 안에 있는 정보가 작은클라스에 있을 때
#큰놈(자식클래스)이 작은놈의 정보를 상속받는다.
#작은놈(부모클래스)은 그대로 두고 
#공격력이 없는 유닛 : 메딕 

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

#공격 유닛 
class AttackUnit(Unit): #공격유닛은 일반유닛에 상속받아서 만들어진거니 self.name, hp를 따로 만들필요없다.
    def __init__(self, name, hp, damage): 
        Unit.__init__(self, name, hp)
        #self.name = name
        #self.hp = hp
        self.damage = damage #부모클래스가 가지고 있는 정보 이외에 추가로 
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}"\
            .format(self.name, location, self.damage))

    def damaged(self,damage):
        print("{o} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage 
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0: 
            print("{0} : 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃", 50 ,16)
firebat1.damaged(25)
firebat1.damaged(25)
