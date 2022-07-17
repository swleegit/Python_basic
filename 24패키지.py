# 패키지 : 모듈을 모아놓은것 
# 현재 디렉토리에 하나의 디렉토리를 만들고 거기에 모듈(.py)파일을 생성한다

import travel.thailand #travel패키지(디렉토리)안에 있는 thailand.py(모듈)을 불러온다
#import travel.thailand.ThailandPackage 
#불가함. from은 없고 import만 있는 경우, import 뒤에는 패키지나 모듈만 가능함, 함수나 클래스를 바로 사용하는 것 안됨 
trip_to = travel.thailand.ThailandPackage() #모듈안에 있는 클래스를 통해 객체를 생성한다
trip_to.detail() #객체를 생성한다음 detail함수를 실행 

from travel.thailand import ThailandPackage #이렇게 from과 같이 엮으면 import 뒤에 함수나 모듈 사용가능함 
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam #travel 패키지에서 vietnam 모듈을 가져온다.
trip_to = vietnam.VietnamPackage()
trip_to.detail()
#                      #from a import b : a는 이제 안써도 됨 b는 써야함 
from travel import * #from 패키지 import * : 이건 불가함, 패키지 안의 여러개의 모듈 중 어디까지 공개할 것인가가 중요함.
#                      #                       공개범위를 지정하는 것은 travel 폴더 안에 __init__파일에 설정하면됨 
#                      #from 모듈 import *: 이건 가능함, 모듈에 있는 모든 함수를 사용한다는 의미

trip_to = vietnam.VietnamPackage()
trip_to.detail()

#패키지, 모듈 위치 확인하기 

import inspect #getfile 함수를 사용하기 위함 
import random #위치를 알고싶은 모듈 or 패키지는  import를 선행해야함
import travel.thailand #thailand는 travel 패키지 안에 있는 모듈이기 때문에 import thailand만 하면 안됨 


print(inspect.getfile(random))
print(inspect.getfile(travel.thailand))