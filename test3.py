# 산술 연산자
# +,-,*,/
# //,%,**

# *,/ +,-
print(15 / 4) # 전체 실수까지 얻고 싶을때
print(15 // 6) # 나눗셈이지만 몫만 얻고 싶을때  (몫)
print(15 % 6) # 나눠서 몫이 아닌 나머지를 얻고 싶을때 (나머지)
print(5**5)

# 가우스 법칙
print((100*101)/2) # 1~100 까지 합
print((10000*10001)/2) # 1~10000 까지 합

# 비교연산자
# == , != , < , > , >= , <=
print(1 == 1 , 1 == 2)
print(1 != 1 , 1 != 2)
print(1 > 1 , 1 > 0)
print(1 < 1 , 1 > 0)
print(1 >= 1 , 1 >= 0)
print(1 <= 1 , 1 <= 0)

# 논리 연산자
# and, or, not
print( True and True )
print( True and False )
print( True or True )
print( True or False )
print( 1 in [1,2,3,4,5])
print( 1 not in [1,2,3,4,5])

a = 1
b = 2
print(type(a) is type(b))
print(type(a) == type(b))

# 복합 할당 연산자
# 산술연산과 할당 연산을 복합적으로 사용하는 연산자
# 변수 a에 존재하는 값의 산술 연산을 수행하고 나온 결과를 변수 a에 재할당
# a += 1 -> 변수 a 의 값에 1을 더하고 변수 a에 재할당
# a -= 1 -> 변수 a 의 값에 1을 빼고 변수 a에 재할당
# a *= 2 -> 변수 a 의 값에 2를 곱하고 변수 a에 재할당
# a /= 2 -> 변수 a 의 값에 2를 나누고 변수 a에 재할당
# a //= 2 -> 변수 a 의 값에 2를 나눈 몫을 변수 a에 재할당
# a %= 2 -> 변수 a 의 값에 2를 나눈 나머지를 변수 a에 재할당
# a **= 2 -> 변수 a 의 값에 거듭제곱 2를 한 후 변수 a에 재할당

a=10
a /= 2
print(a)

a=10
a //= 2
print(a)

a=10
a %= 2
print(a)

a=10
a **= 2
print(a)
a=10
a **= 3
print(a)

#문1) 600kg 제한의 화물용 엘리베이터가 있다. 2개의 물건에 대한 
#무게를 실수로 입력 받아 현재 엘리베이터에 적재 할 수 있는
#무게를 구하고 출력 하시오.
#   입력 양식
#       첫 번째 물건의 무게 : 200.5
#       두 번째 물건의 무게 : 78.56

#   출력 양식
#       화물 엘리베이터의 허용 무게 320.94kg 남았습니다.


box = 600
fi_pro, se_pro = float(input("first: ")),float(input("second: "))
po_ar = box - (fi_pro + se_pro)
print('max 제한 무게{} , 현재 사용중 인 중량 {}, 앞으로 더 사용할 수 있는 중량 {} '
.format(box, fi_pro + se_pro,po_ar))

print('화물 엘리베이터의 허용 무게 {}'.format(po_ar))

#찬솔씨
a = input("물건의 A의 무게?")
b = input("물건의 B의 무게?")

허용무게 = 600 - float(a) - float(b)
print(f'화물 엘레베이터의 무게는{허용무게}kg 남았습니다.')



#문2) 현재 원달러 환율이 1,121.3원 일때 n원을 달러로
# 환전하는 경우 몇 달러가 되는지 구하는 코드를 작성 하시오.

n = int(input("원화: "))
dol = 1121.3
print('{}원를 달러로 환전 하면{:,.2f} 이다'.format(n,n/dol))


#준씨
#환율 = float(input("현재 환율 : "))
#won = int(input("교환 : "))
#doallars = int(won)/float(환율)
#print('원 대비 달러는 {:,.2f}달러 입니다.').format(doallars))








