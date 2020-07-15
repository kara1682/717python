# input 함수
m1 = input("Message: ")
print(type(m1))
print(m1)

# 사용자로부터 이름, 키 ,체중 값을 입력 받아 비만도를 구하고 출력하는 코드를 작성하시오.
# 비만도 계산 식 : 비만도(%) = 현재체중 / 표중체중 * 100
# 표준 체중 계산 식 : 표준 체중 = (현재 키 - 100) * 0.9
# 출력 예제 : 홍길동님의 비만도는 112.15% 입니다.


#name = input("name: ")
#height = int(input("height: "))
#weight = int(input("weight: "))

#pw = (height - 100) * 0.9 # 표준 체중
#bmi = weight / pw * 100 # 비만도
#print('{}님의 비만도는 {:.2f}%입니다.'.format(name,bmi))

#보성씨의 방법
n, h, w = input("name: "),int(input("height: ")),int(input("weight: "))
print('{}님의 비만도는 {:.2f}%입니다.'.format(n,100*w/(h-100)*0.9))
