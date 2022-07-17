#모듈
#어떠한 기능이 있는 함수, 클래스 꾸러미
#확장자는 .py
#모듈이 같은 라이브러리에 있어야 불러올 수 있다.
#또는 C:\Users\이승우\AppData\Local\Programs\Python\Python39\lib\ 이 내부에 있으면 가능하다

import theater_module

theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *

price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning

price(3)
price_morning(4)
##price_soldier(5) --> 이건 오류 발생 

from theater_module import price_soldier as price

price(3) # = theater_module.price_soldier






