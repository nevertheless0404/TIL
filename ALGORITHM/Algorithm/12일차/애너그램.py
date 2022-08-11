# https://www.acmicpc.net/problem/6996

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220811/애너그램.txt")

n = int(input())
for _ in range(n):
    a, b = input().split()
    if len(a) != len(b):
        print(f'{a} & {b} are NOT anagrams.')
        continue
    arr_a, arr_b = sorted(a), sorted(b)

    if arr_a == arr_b:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')



