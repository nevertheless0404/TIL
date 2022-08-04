# https://www.acmicpc.net/problem/11945

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220804/뜨거운 붕어빵.txt")

n, m = map(int, input().split())

# 행으로 붕어빵의 모양을 입력 
for tc in range(n):
    print(input()[::-1])