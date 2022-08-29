# https://www.acmicpc.net/problem/14467

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220810/소가 길을 건너간 이유1.txt")

n = int(input())
cow_dict = dict()
move = 0
for _ in range(n):
    cow, location = map(int, input().split())
    if cow in cow_dict.keys():
        # 소가 오른쪽에 없으면 증가 
        if location != cow_dict[cow]:
            move += 1
            cow_dict[cow] = location
    else:
        cow_dict[cow] = location
print(move)