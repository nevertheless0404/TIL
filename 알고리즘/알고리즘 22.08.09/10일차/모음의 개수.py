# https://www.acmicpc.net/problem/1264

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220809/모음의 개수.txt")

while True:
    sentence = input()
    count = 0
    # 입력 끝
    if sentence == '#':
        break
    for i in sentence:
        # 모음이 들어가면 증가
        if i in 'aeiouAEIOU':
            count += 1
    print(count)