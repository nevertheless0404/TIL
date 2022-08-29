# https://www.acmicpc.net/problem/1269

import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220802/대칭 차집합.txt")

n_a, n_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a-b)+len(b-a))