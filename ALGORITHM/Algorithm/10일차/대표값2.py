# https://www.acmicpc.net/problem/2587

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220809/대표값2.txt")

num = []
for i in range(5):
    num.append(int(input()))

print(int(sum(num)/5))
num.sort()
print(num[2])