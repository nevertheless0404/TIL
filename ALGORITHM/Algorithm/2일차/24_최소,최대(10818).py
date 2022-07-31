# https://www.acmicpc.net/problem/10818

import sys
sys.stdin = open("/Users/yuyeong/Desktop/TIL/자료구조 22.07.26/25_최소,최대(10818).txt","r")


cnt = int(input())
# 정수를 입력 받고, input().split을 이용하여 공백으로 구분
number = list(map(int, input().split()))
print(min(number),max(number))

