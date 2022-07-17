#이전 21파일에서는 원래 ValueError은 값을 잘못입력했을 때 나오는 문구인데 
#두자리 숫자도 ValueError로 처리함. 즉 잘못입력하거나 두자리를 입력한 경우 둘다 동일한 에러로 처리됨
#그냥 두자리숫자를 입력한 경우를 내가 따로 에러처리를 하고 싶은 경우 

class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self): #이것도 BigNumberError이 발생할 때 실행됨 
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0} , {1}".format(num1, num2)) #msg에 이 값을 대입하게됨 
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력했습니다. 한자리 숫자만 입력하세요.")

except BigNumberError as err: #raise를 만나면 일로 내려오고 여기로 리턴값을 넘김 
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

finally:
    print("계산기를 이용해 주셔서 감사합니다.")
    #try든 except든 어느게 실행되고 가장 마지막에 무조건적으로 실행을 함 
 
  
