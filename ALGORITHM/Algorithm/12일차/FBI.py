# https://www.acmicpc.net/problem/2857

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220811/FBI.txt")

data = []
for i in range(5):
    data.append(input())
cnt = 0
for i in range(5):
    if 'FBI' in data[i]:
        print(i+1, end = ' ')
        cnt = 1
if cnt == 0:
    print("HE GET AWAY!")