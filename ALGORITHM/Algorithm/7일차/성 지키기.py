# https://www.acmicpc.net/problem/1236

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220803/성 지키기.txt")

n,m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

row_count = []
col_count = []

for i in range(n):
    # 행 범위 내에 X 가 없으면 추가 
    row_count.append('X' not in board[i])

for j in range(m):
    # 열 범위 내에 i와 j 값을 고정 시키고 없으면 추가 
    col_count.append('X' not in [board[i][j] for i in range(n)])

# 경비원이 없는 행과 열의 수를 출력하고, 거기서 가장 큰 값이 답이다.
print(max(sum(row_count), sum(col_count)))