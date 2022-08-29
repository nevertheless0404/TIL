# https://www.acmicpc.net/problem/10101

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220810/삼각형 외우기.txt")

a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:
    print("Equilateral")
elif a + b + c == 180:
    if a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")