# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘01/01-ALGORITHM/1회차/김유영/20220725/3_OX퀴즈.txt")
n = int(input())
# O 일때, 연속하여 몇 번 O가 들어가는지 카운트
for oh in range(n):
    count = 0
    sum = 0
    a = list(input())
    # 0 일때, 임의의 변수로 카운트한 수를 더함
    for i in a:
        if i == 'O': # OX가 O일때
            count += 1
            sum = sum + count
        else:
            count = 0

    print(sum)