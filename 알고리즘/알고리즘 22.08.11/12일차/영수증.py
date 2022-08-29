# https://www.acmicpc.net/problem/25304

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220811/영수증.txt")

x = int(input())
n = int(input())

cnt = 0
for i in range(n):
    a,b = map(int, input().split())
    c = a*b
    cnt += c

if x == cnt:
    print("Yes")
else:
    print("No")

