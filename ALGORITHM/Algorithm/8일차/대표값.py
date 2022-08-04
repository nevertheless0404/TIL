# https://www.acmicpc.net/problem/2592

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220804/대표값.txt")

number = [int(input()) for _ in range(10)]
print(sum(number)//10)
# max를 구할 때 key 파라미터를 이용해 최빈값 구함 
print(max(number, key = number.count))