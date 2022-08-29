# https://www.acmicpc.net/problem/11286

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220802/절대값 합.txt")
import heapq

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            # 절대값이 가장 작은 값 출력 및 제거 
            print(heapq.heappop(heap)[1])
        # 비어있는 경우
        else:
            print(0)
    else:
        # 값 추가 
        heapq.heappush(heap,((abs(x)),x))
