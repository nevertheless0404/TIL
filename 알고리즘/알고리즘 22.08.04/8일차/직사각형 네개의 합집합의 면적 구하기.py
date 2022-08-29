# https://www.acmicpc.net/problem/2669

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220804/직사각형 네개의 합집합의 면적 구하기.txt")

# 100 * 100 배열 도화지 만들기
drawing = [[0]*100 for _ in range(101)]

# 네개의 직사각형을 도화지에 넣어줌
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    # 행, 열 모아주기
    # 직사각형이 만들어졌으면 1로 바꿔주기
    for i in range(x1, x2):
        for j in range(y1, y2):
            drawing[j][i] = 1

# 만들어진 직사각형을 면적을 더 해주기!
count = 0
for k in drawing:
    count += sum(k)

print(count)