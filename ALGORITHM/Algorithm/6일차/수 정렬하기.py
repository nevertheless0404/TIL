# https://www.acmicpc.net/problem/2750

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220802/수 정렬하기.txt")

n = int(input())
num =[]
for i in range(n):
    # 숫자들을 리스트에 담기
    num.append(int(input()))

num.sort() # 오름차순 정렬

# 정렬된 숫자들 한개씩 출력
for j in num:
    print(j)
