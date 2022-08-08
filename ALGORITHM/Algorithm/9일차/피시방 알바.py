# https://www.acmicpc.net/problem/1453

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220808/피시방 알바.txt")

n = int(input())
# 손님이 앉고 싶어하는 자리 
seat = list(map(int, input().split()))
# 피씨방 자리
pc_space = []
#거절당한 사람의 수 
refusal = 0

for i in range(n):
    if seat[i] in pc_space:
        refusal += 1
    else:
        pc_space.append(seat[i])
print(refusal)
