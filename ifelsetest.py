# if ...else 유형

# 계정 생성 프로그램을 작성 하세요.
# 1. 사용자로 부터 계정을 생성하기 위한 ID 와 PW를 입력 받습니다.
# 2. PW의 경우 한번 더 사용자 입력을 받아서 이전에 입력한 PW와 일치한 
#    PW를 입력 하였는지를 확인하여 일치한 경우에만 "계정 생성 완료
#    " 메시지를 출력하고 그렇지 않은 경우에는 "계정 생성 실패 메시지
#    를 출력하게 하세요.


id, pw = input("ID를 입력하세요: "), input("PW를 입력하세요.: ")
pwch = input("PW를 다시한번 입력하세요.: ")

if pw == pwch:
    print("계정 생성 완료")
else :
    print("계정 생성 실패")
