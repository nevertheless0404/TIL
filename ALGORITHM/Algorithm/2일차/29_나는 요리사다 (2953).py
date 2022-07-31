# https://www.acmicpc.net/problem/2953

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220726/29_나는 요리사다.txt","r")

max = 0
max_i = 0
for i in range(1, 6):
    # 각 숫자 리스트의 합을 구함
    # 정수를 입력 받고, input().split()를 이용해 공백으로 구분 후 더함
    score_sum = sum(list(map(int, input().split())))
    if score_sum > max:   # 가장 많은 점수를 얻은 사람
        max = score_sum

print(max_i, max)
