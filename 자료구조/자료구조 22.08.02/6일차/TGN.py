# https://www.acmicpc.net/problem/5063

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220802/TGN.txt")
input = sys.stdin.readline

n = int(input())

for test_case in range(n):
    r, e, c = map(int, input().split())
    if r < e-c:
        print("advertise")
    elif r == e-c:
        print("does not matter")
    else:
        print("do not advertise")