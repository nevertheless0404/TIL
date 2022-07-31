# https://www.acmicpc.net/problem/2846

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220726/28_오르막길.txt")

n = int(input())
road = list(map(int, input().split()))

tmp = 0  # 오르막길 경사 누적값 담을 임시 변수 
max_m = 0  # 갱신할 최대값 변수

for i in range(1, n):   # 앞 뒤를 비교, 1부터 시작
    slope = road[i] - road[i-1]  # 경사 차이
    if slope >= 1:  # 오르막이라면
        tmp += slope   # 경사 차이를 누적시켜 준다.
    else:    # 내리막길을 만나면
        tmp = 0  # 초기화!

    if max_m < tmp:    # 최대값 갱신
        max_m = tmp

print(max_m)
