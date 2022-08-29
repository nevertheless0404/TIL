# https://www.acmicpc.net/problem/2167

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220803/2차원 배열의 합.txt")

n, m = map(int, input().split())
lst = []
# dp를 우선 초기화 시켜주기
dp = [[0] * (m+1) for _ in range(n+1)]
for _ in range(n):
    lst.append(list(map(int, input().split())))

# dp 생성하기 
# 누적값 생성
for i in range(1, n+1):
    for j in range(1, m+1):
        # dp[a-1][b-1]은 앞에 dp 누적합을 구할 때 중복 사용되서 빼준다.
        # 본래값 + 왼쪽 + 위쪽 - 대각선
        dp[i][j] = lst[i-1][j-1]+dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]

# 문제 값 계산
k = int(input())
for _ in range(k):
    i,j,x,y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]) 

# 2. 
# i -= 1
# j -= 1
# x -= 1
# y -= 1
# sum_ = 0

# 이중 반복문
# i -> x
# for r in range(i, x+1):
# j -> y
# for c in range(j, y+1):
# sum_+= lst[r][c]
# print(sum_)