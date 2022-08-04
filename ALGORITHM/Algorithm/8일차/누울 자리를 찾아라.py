# https://www.acmicpc.net/problem/1652

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220804/누울 자리를 찾아라.txt")
input = sys.stdin.readline

n = int(input())
room = []
for _ in range(n):
    room.append(list(input()))

row, column = 0, 0
for i in range(n):
    count = 0
    for j in range(n):
        # '.'를 만나면 증가
        if room[i][j] == '.':
            count += 1
            # 'x'를 만나면 그동안 증가 시킨것이 2 이상이면 
            # 가로줄에 누울 자리를 추가! 아니면 초기화
        elif room[i][j] == 'X':
            if count >= 2:
                row += 1
            count = 0
    if count >= 2:
        row += 1
    count = 0

for i in range(n):
    count = 0
    for j in range(n):
        if room[j][i] == '.':
            count += 1
        elif room[j][i] == 'X':
            if count >= 2:
                column += 1
            count = 0
    if count >= 2:
        column += 1
    count = 0

print(row, column)
 
   
    
