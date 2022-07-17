#예외발생 

try:
    print("나누기 전용 계산기입니다.")
    nums =[]
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입려하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError: #try구문을 실행하다가 ValueError 발생하면 아래구문을 실행시킴
    print("에러! 잘못된 값을 입력했습니다")

except ZeroDivisionError as err: # ZeroDivisionError를 err 변수에 할당한다는 의미
    print(err)

#except: #위에 두가지 에러가 아닌경우에 아래 코드 실행한다.
    #print("알 수 없는 에러가 발생하였습니다.")

except Exception as err: #위에 두가지 에러가 아닌 경우, 그리고 그 에러가 어떤건지 알고 싶은 경우
    print("알 수 없는 에러가 발생했습니다")
    print(err)

#일부로 에러 발생시키기 : 문법상으로는 문제없지만 사용자가 지정한 것에 벗어나면 에러로 규정하는 것 

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요."))
    num2 = int(input("두 번째 숫자를 입력하세요."))
    if num1 >= 10 or num2 >= 10:
        raise ValueError #이 구문을 만나면 try의 나머지 구문은 실행하지 않고 except에 처리한
                         #value error로 넘어가서 예외처리를 한다. 
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력했습니다. 한자리 숫자만 입력하세요.")

  
