#파일 입출력 : 외부 파일을 읽고, 쓰기

#score.txt라는 파일을 만들고(기존에 있다면 기존내용 리셋) 내용을 작성하기

score_file = open("score.txt", "w", encoding = 'utf8') #확장자명 반드시 포함, 모드, 한글이라면 encoding 정보
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close() #파일을 열었으면 닫는것까지 하자 

#기존내용에 추가
score_file = open("score.txt", "a", encoding='utf-8')
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #변수.write()을 할때는 자동 줄바꿈이 안되니 탈출문자로 따로 해야함
score_file.close()

#기존내용 전체 읽어들이기
score_file = open("score.txt", "r", encoding='utf8')
print(score_file.read()) #파일 내용 전체를 읽어들이기, print를 사용해야 모니터에 출력된다.
score_file.close()

#기존내용 한줄씩 읽어들이기 (몇줄인지 아는 경우)
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end = ' ') #readline자체로 한줄을 읽어들인다음 커서를 다음줄로 옮기는데 print도 다음줄로 옮기니 문장간에 한칸 엔터가 생김, 그래서 end = " "사용
print(score_file.readline(), end = ' ')
print(score_file.readline(), end = ' ')
print(score_file.readline(), end = ' ')
score_file.close()

#기존내용 한줄씩 읽어들이기 (몇줄인지 모르는 경우)
score_file = open("score.txt", "r", encoding='utf8') #파일 처리(읽기, 쓰기) 하려면 반드시 앞에 선언하고 시작
while True:
    line = score_file.readline() #귀찮으면 이걸 변수로 사용해서 
    if not line: #line의 내용이 없다면 False, not False = True
        break
    print(line,end= ' ')
score_file.close()

#다른 방법 한줄씩 모아서 리스트로 저장
score_file = open("score.txt", "r", encoding='utf8')
lines = score_file.readlines() #리스트 형태로 저장, 커서가 다음으로 이동해 있는 것도 저장되어 있음
for line in lines: #원소(단수) 리스트 (복수)
    print(line, end="")
score_file.close()





