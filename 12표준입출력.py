#표준 입출력 

print("python", "java", 'java script', sep = 'vs', end ='?')
print("무엇이 더 재미있을까요?")
#print함수에서 변수가 ,로 연결되어있을 때 디폴트 출력은 띄어쓰기 이지만
#sep = '원하는것' 를 통해 띄어쓰기를 원하는 것으로 대체할 수 있다.
#end = '?'를 통해 print 마지막이 ?로 끝나고 줄바꿈해서 커서를 옮기는게 아니라 바로 뒤에 커서를 놓는다
#따라서 이어서 나오는 print구문이 곧바로 연이어 출력된다.

#이 부분은 무슨말인지 모르겠음.
import sys
#visual studio상에서는 이들의 출력 결과차이는 없어보이지만
print("python", "java", file=sys.stdout) #표준출력으로 문장이 출력 
print("python", "java", file=sys.stderr) #표준 에러로 처리되는 것
#로그처리를 따로 할때 error같은 경우는 따로 확인해서 수정한다.

#정렬해서 출력하기, 딕셔너리.items

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items(): # subject, score = (key, value)와 같음, 각각 대응됨
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ':')
    #문자열.ljsut(n) n자리만큼 자리를 확보한다음 해당문자열을 왼쪽 정렬함.
    #score은 숫자이기에 문자열함수를 사용하기 위해 문자열로 전환

#은행 대기순번표
#001,002,003 ... 
for num in range(1,21):
    print("대기번호: "+str(num).zfill(3)) # 문자열.zfill(n) n개의 공간 중 해당 문자열을 제외한 나머지는 0으로 채운다.

#input: 사용자에게 받은 입력값을 변수에 할당할 수 있다.

answer = input("아무 값이나 입력해보세요: ") #숫자를 입력해도 문자형으로 받는다.
print(type(answer)) # type<str>
print("입력하신 값은 "+answer+ "입니다.") #str(answer)안해도 됨 