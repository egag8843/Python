"""
날짜 : 2021/04/30
이름 : 장경준
내용 : 파이썬 패키지와 모듈 실습하기 교재 p175
"""
import Ch06.sub2.calc
import Ch06.sub2.calc as c
from Ch06.sub2.calc import *

r1 = Ch06.sub2.calc.plus(1, 2)
r2 = c.minus(2, 3)
r3 = multi(3, 4)
r4 = div(4, 2)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)


