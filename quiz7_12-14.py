'''
quiz)
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

-x 주차 주간보고 -
부서 : 
이름 : 
업무 요약:

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오 

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
'''

#풀이

for week in range(1,51): # 1 ~ 50
    with open("{0}주차.txt".format(week), "w", encoding= 'utf8') as file_report:
        print(f"-{week} 주차 주간보고-", file = file_report)
        file_report.write("부서 :\n이름 :\n업무 요약:")

#해답 

for i in range(1,51):
    with open(str(i) + ".txt", "w",encoding="utf8") as file_report:
        file_report.write("-{0} 주차 주간보고 -".format(i))
        file_report.write("부서 :\n이름 :\n업무 요약:")
        #문자열.format : 문자열 함수임! print구문 안에서만 사용해야하는거 아니다.
