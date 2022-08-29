# https://www.acmicpc.net/problem/2693


import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220804/N번째 큰 수.txt")

t  = int(input())
for _ in range(t):
    num = list(map(int, input().split()))
    num.sort() # 오름차순으로 배열
    print(num[-3]) # 3번째 출력 