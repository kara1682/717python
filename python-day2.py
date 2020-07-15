# -*- coding: utf-8 -*-

a = 10
b1, b2 = 20, 30
c1, c2, c3 = 40, 'variable', 50.5
print(a)
print(a + b1)
print(b2 - b1)

print(type(a))
print(type(c2))
print(type(c3))

a = '10'
print(type(a))

a = 10.0
print(type(a))

p1, p2, p3 = '010','8888','9999'
pp1 = int(p1)
print(p1)
print(type(p1))
print(type(pp1))

pp1 = pp1 + 10
print(pp1)

#
num1, num2 = 10, 20
name, age = 'Yangchanghee', 30
print('{} + {} = {}'.format(num1, num2, num1 + num2))
print('이름 : {}\n나이 : {}'.format(name, age))


english, math, korean = 100, 70, 90
tot = english + math + korean
avg = tot / 3
print('합계 : {}\n평균 : {:.2f}'.format(tot, avg))



