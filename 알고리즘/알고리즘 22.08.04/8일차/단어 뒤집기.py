# https://www.acmicpc.net/problem/9093

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220804/단어 뒤집기.txt")

for _ in range(int(input())):
    en = input().split()
    for i in en:
        print(i[::-1], end =" ")
    print()