# https://www.acmicpc.net/problem/9012

import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220801/괄호.txt")

input = sys.stdin.readline
n = int(input())
for test_case in range(n):
    # 괄호 리스트 
    list = input()
    count = 0

    for i in list:
        # '(' 가 나오면 1을 더해주고
        if i == '(':
            count += 1
        # ')' 가 나오면 1을 빼줘서 
        elif i == ')':
            count -= 1
        # 조건을 만족하지 못할 떄는 나와!!!!
        if count < 0:
            break
# 0이 나와야 한다.
    if count == 0:
        print("YES")
    else:
        print("NO")

       