# https://www.acmicpc.net/problem/2231

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220726/27_분해합.txt")

N = int(input())
result = 0
for i in range(1, N+1): # 모든 경우의 수를 비교 
    # 우선 i 문을 문자형으로 받고, 정수형으로 바꿔 각 자리의 합을 구한다.
    hap = list(map(int, str(i)))
    # 그리고 i의 값과 각 자리 수의 값도 더 한다.
    S = i + sum(hap)
    # 합이 입력한 값과 동일하면 종료
    if (S == N):
        result = i
        break

print(result)
