# https://www.acmicpc.net/problem/3046

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220808/R2.txt")

r1, s = map(int, input().split())
print(s * 2 - r1)