# 실수 2개(a, b)를 입력받아
# a를 b번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

from unittest import result


a, b = input().split()
result = float(a) ** float(b)
print(result)