# https://www.acmicpc.net/problem/1547

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220804/공.txt")

n = int(input())
cups = [1, 2, 3]
for _ in range(n):
    x, y = map(int, input().split())

    i = cups.index(x)
    j = cups.index(y)

    cups[i], cups[j] = cups[j], cups[i]

print(cups[0])