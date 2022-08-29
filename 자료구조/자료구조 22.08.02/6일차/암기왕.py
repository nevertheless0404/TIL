# https://www.acmicpc.net/problem/2776

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220802/암기왕.txt")

t = int(input())
for tc in range(t):
    n = int(input())
    # 수첩 1에 있는 값은 중복값이 없게 만들었다.
    num_n = set(map(int, input().split()))
    m = int(input())
    num_m = list(map(int, input().split()))
    # 반복문을 이용해 수첩 2에 있는 숫자를 확인
    for numbers in num_m:
        if numbers in num_n:
            print(1)
        else:
            print(0)
