
# https://www.acmicpc.net/problem/1110

import sys
sys.stdin = open("/Users/yuyeong/Desktop/TIL/자료구조 22.07.26/2_더하기 사이클(1110).txt","r")

N = int(input())
num = N
count = 0

while True:
    count += 1
    sum = N//10 + N%10
    N = N%10*10 + sum%10
    if (N == num):
        break

print(count)