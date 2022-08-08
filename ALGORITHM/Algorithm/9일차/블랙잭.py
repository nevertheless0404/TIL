# https://www.acmicpc.net/problem/2798

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220808/블랙잭.txt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

blackjack = 0

# 3중 반복문으로 반복 추출이 없게 뽑아야 한다.
for i in range(n):
    # i 값 보다 크게
    for j in range(i+1, n):
        # j 값보다 크게 
        for k in range(j+1, n):
            #  3개의 값을 더한것이 m 보다 크면 넘어감
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                blackjack = max(blackjack, arr[i]+arr[j]+arr[k])
                
print(blackjack)