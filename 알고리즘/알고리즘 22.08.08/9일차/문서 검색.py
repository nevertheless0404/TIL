# https://www.acmicpc.net/problem/1543

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220808/문서 검색.txt")

# 1. 
a = input()
b = input()
cnt = 0
n = 0

# 최대 a의 길이에서 b의 길이를 뺀다. 
# 에졔 1번으로 따지면 최대 7번꺠 자리까지 갈 수 있는데 
# 인덱스로는 6 에 해당됨
while n <= len(a) - len(b):
    # b길이만큼 자른 a가 같다면 증가
    # 인덱스 n의 길이만큼 더함 
    if a[n:n + len(b)] == b:
        cnt += 1
        n += len(b)
    else:
        n += 1
print(cnt)

# 2.
# print(input().count(input()))


