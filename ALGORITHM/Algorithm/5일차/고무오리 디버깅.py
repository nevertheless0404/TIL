# https://www.acmicpc.net/problem/20001

import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220801/고무오리 디버깅.txt")

start = input()
question = 0
while True:
    # 문제 혹은 끝나는 걸 입력 
    rubberduck = input()
    # 문제가 끝나면 탈룩
    if rubberduck == "고무오리 디버깅 끝":
        break
    else:
        if rubberduck == "문제":
            question += 1
            # 고무오리를 입력했는데 문제가 0개이면 벌칙으로 2개
        elif rubberduck == "고무오리":
            if question == 0:
                question += 2
            else:
                question -= 1
if question == 0:
    print("고무오리야 사랑해")
else:
     print("힝구")