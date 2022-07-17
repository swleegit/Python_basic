#import를 해서 사용함 
#구글에 list of python modules를 검색해서 외장 모듈을 확인할 수 있음

#대표적인 외장함수

#glob : 경로 내의 폴더/ 파일 목록 조회
import glob
print(glob.glob("*.py")) # 현재 위치한 디렉토리에 확장자가 py인 모든 파일

#os : 운영체제에서 제공하는 기본 기능

import os
print(os.getcwd()) #현재 작업디렉토리 경로 

folder = "sample_dir"

if os.path.exists(folder): #현재 디렉토리에 해당 폴더가 있으면 True를 반환 
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) #해당 이름을 가진 폴더를 현재 디렉토리에 생성 
    print(folder , "폴더를 생성하였습니다.")

print(os.listdir()) #현재 디렉토리에 있는 파일과 폴더 리스트 

#time : 시간관련함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H: %M: %S"))

#datetime
import datetime
print("오늘 날짜는 ", datetime.date.today()) #오늘 년 월 일 

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today() #오늘 날짜 저장 
td = datetime.timedelta(days = 100) # 100일 저장 
print("우리가 만난지 100일은", today + td) #오늘부터 100일 후

