# https://www.acmicpc.net/problem/11170

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220808/0의 개수.txt")

t = int(input())
for tc in range(t):
    count = 0
    n, m = map(int, input().split())
    # n부터 m까지 반복
    for i in range(n , m+1):
        # 현재 숫자를 문자열 형대로 변환
        num = str(i)
        count += num.count('0')
    print(count)