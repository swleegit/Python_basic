class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

FlyableUnit()

#출력결과는 "Flyable 생성자"
#다중상속에서 super을 사용하면 가장 앞의 부모클래스만 적용됨 