# https://www.acmicpc.net/problem/2495

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220811/연속구간.txt")

for i in range(3):
    n = input()
    # 연속구간이 없는것은 1로 초기화
    max_n = 1
    cnt = 1
    for j in range(1, len(n)):
        # 지금수와 바로 뒤에 숫자가 같다면 증가
        if n[j] == n[j-1]:
            cnt += 1
        else:
            # 연속해서 같은 숫자가 없으면 1
            max_n = max(cnt, max_n)
            cnt = 1
    max_n = max(cnt, max_n)
    print(max_n)





