# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.

a, b = input().split()
a = int(a)
b = int(b)
sum = a + b
sub = a - b
mul = a * b
Q = a // b
R = a % b
div = a / b

print(sum)
print(sub)
print(mul)
print(Q)
print(R)
print(format(div, ".2f"))