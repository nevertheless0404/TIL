# https://www.acmicpc.net/problem/5533

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220803/유니크.txt")

n = int(input())
scroe = [[], [], []]
sum = []
for _ in range(n):
    # 열의 점수를 넣어준다. 
    a, b, c = map(int, input().split())
    scroe[0].append(a)
    scroe[1].append(b)
    scroe[2].append(c)
    # 행값은 받아올꺼니 우선 초기화
for i in range(n):
    cnt = 0
    for j in range(3):
        # 행과 열을 같이 
        # 개수가 1개인 것을 확인하고 
        if scroe[j].count(scroe[j][i]) == 1:
            cnt += scroe[j][i]
        # 더한 숫자를 sum리스트에 담아줌 
    sum.append(cnt)
for i in sum:
    print(i)