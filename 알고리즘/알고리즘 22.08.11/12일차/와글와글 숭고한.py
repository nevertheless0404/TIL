# https://www.acmicpc.net/problem/17388

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220811/와글와글 숭고한.txt")

s, k, h = map(int, input().split())
if s + k + h >= 100:
    print("OK")
else:
    if min(s, k, h) == s:
        print("Soongsil")
    elif min(s, k, h) == k:
        print("Korea")
    else:
        print("Hanyang")
        