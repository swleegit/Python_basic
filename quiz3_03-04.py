'''
quiz)사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 =>naver.comp
규칙2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 개수 + "!"로 구성
                (nav)                  (5)            (1)              (!)    

예)생성된 비밀번호 : nav51!           
'''

#내가 푼 답안 

# site = "http://naver.com" #7부터
# dot = site.index(".")
# site_re = site[7:dot] #규칙2
# three = site_re[:3]
# num_total = len(site_re)
# num_e = site_re.count("e")
# password = three + str(num_total) + str(num_e) + "!"
# print(f"생성된 비밀번호: {password}")

#해답

url = "http://naver.com"
my_str = url.replace("http://","") #할당값을 변화시키지 못하기 때문에 새로운 변수를 지정 
#print(my_str) #중간중간 체크해가면서
my_str = my_str[:my_str.index(".")] #[0:5] : 0,1,2,3,4
#결국에 naver만 필요함, 변수를 새롭게 지정하지말고 위에서 썼던 것에서 내용만 새롭게 할당하는식
#변수 선언을 적당히 간소화, 한번에 진행, 너무 복잡하면 적당히 끊고 아래서 선언하는 방식으로 진행 
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
#{변수이름}하려면 안에서 선언해야함.
#밖의 변수 f"" or 위에 처럼 