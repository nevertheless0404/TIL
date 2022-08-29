# https://www.acmicpc.net/problem/2902

import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220801/KMP는 왜 KMP일까?.txt")

date = list(input().split('-'))
for i in date:
    print(i[0], end='')