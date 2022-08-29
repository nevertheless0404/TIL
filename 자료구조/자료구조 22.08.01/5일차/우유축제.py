# https://www.acmicpc.net/problem/14720

import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220801/우유축제.txt")

n = int(input())
milk = list(map(int, input().split()))
count = 0

for i in range(n):
    if milk[i] == count % 3:
        count += 1

print(count)