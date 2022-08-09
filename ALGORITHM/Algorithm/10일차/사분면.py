# https://www.acmicpc.net/problem/9610

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220809/사분면.txt")

n = int(input())
axis = 0
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        Q1 += 1
    elif y > 0 > x:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 > y:
        Q4 += 1
    elif x == 0 or y == 0:
        axis += 1
print("Q1: "+str(Q1))
print("Q2: "+str(Q2))
print("Q3: "+str(Q3))
print("Q4: "+str(Q4))
print("AXIS: "+str(axis))