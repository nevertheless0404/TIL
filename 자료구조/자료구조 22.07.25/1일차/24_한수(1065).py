# https://www.acmicpc.net/problem/1065

import sys
sys.stdin = open("/Users/yuyeong/Desktop/TIL/자료구조 22.07.26/24_한수(1065).txt","r")

num = int(input())
hansu = 0
for i in range(1, num + 1):
    # i 문을 문자형으로 받고, 정수형으로 바꿔준다.
    num_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1  # 100보다 작으면 모두 한수
        # 연속된 두 개의 수의 차이가 일정한 수열 
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu +=1  # x의 각 자리가 등차수열이면 한수

print(hansu)
