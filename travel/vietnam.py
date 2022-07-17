class VietnamPackage:
    def detail(self):
        print("[배트남 패키지 3박 5일] 다낭 효도 여행 60만원")

#모듈을 외부에서 사용하는지, 아니면 모듈 자체를 직접 실행하는지 구분하기 위해서

if __name__ == "__main__":
    print("Vietnam 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = VietnamPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
    