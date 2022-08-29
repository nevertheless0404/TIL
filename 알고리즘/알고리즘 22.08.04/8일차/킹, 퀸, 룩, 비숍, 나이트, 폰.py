# https://www.acmicpc.net/problem/3003

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220804/킹, 퀸, 룩, 비숍, 나이트, 폰.txt")

origin = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split()))
for i in range(6):
    print(origin[i]-chess[i], end= " ")