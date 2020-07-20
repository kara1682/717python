'''
조건문 if
조건이 참일때 실행.


if 조건식:
    실행 코드 1
    실행 코드 2
    if 조건식:
        실행 코드 1
        실행 코드 2


if 조건식:
    실행 코드 1
elif 조건식:
    실행 코드 2
elif 조건식:
    실행 코드 2
else :
    실행 코드 2



# 랜덤 함수
from random import random
from random import randint
from random import randrange

# a = random()          # 0.0 ~ 1.0 미만
# a = random() * 10     # 0.0 ~ 10.0 미만
# a = int(random() * 10)
a = randint(10,19)    # 10 ~ 20 미만
b = randrange(11,20,2)
print(a,b)


from random import random
num = int(random() * 100)
print(num)
if num > 50:
    print("50보다 크다")
if num <= 50:
    print("50보다 작거나 같다")

if num % 2 == 0:
    print("num은 짝수 입니다.")
elif num % 2 == 1:
    print("num은 홀수 입니다.")
    '''

forecast = int(input("오늘 비가 올 확율은 %인가요: "))
if forecast >= 50:
    print("우산을 준비하세요")
else:
    print("친구를 만나세요")

weather = input("오늘 날씨 어때요?: (화창,비,눈,흐림,안개,미세먼지,태풍)")

if weather in ("눈,비,흐림"):
    print("우산을 준비하세요")
elif weather in ("안개,미세먼지"):
    print("마스크를 준비하세요")
elif weather == "화창":
    print("친구를 만나세요")
else:
    print("Stay home")