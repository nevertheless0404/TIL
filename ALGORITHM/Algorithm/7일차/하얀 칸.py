# https://www.acmicpc.net/problem/1100

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220803/하얀 칸.txt")

white = []
for _ in range(8):
    line = list(input())
    white.append(line)
cnt = 0
for i in range(8):
    for j in range(8):
        # 하얀칸일 경우
        # 짝수로만 이루어져있다.
        if (i+j) % 2 ==0:
            # F인경우 더해주기 
            if white [i][j] == 'F':
                cnt += 1
print(cnt)