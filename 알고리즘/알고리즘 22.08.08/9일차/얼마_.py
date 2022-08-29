# https://www.acmicpc.net/problem/9325

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220808/얼마?.txt")

t = int(input())
for tc in range(t):
    s = int(input())
    n = int(input())
    if n == 0:
        print(s)
    else:
        option = 0
        for _ in range(n):
            q,p = map(int,input().split())
            option += q*p
        
        print(s + option)


