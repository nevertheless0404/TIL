# https://www.acmicpc.net/problem/2908

import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘01/01-ALGORITHM/1회차/김유영/20220725/1_상수.txt")


a, b = input().split()
# 상수는 다른 사람과 다르게 거꾸로 수를 읽는다. 
# 그래서 값을 뒤집어 준다.
a = a[::-1]
b = b[::-1]
print(max(a,b))
