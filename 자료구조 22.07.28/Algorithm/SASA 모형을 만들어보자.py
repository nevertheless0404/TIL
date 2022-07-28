# https://www.acmicpc.net/problem/23825


N, M = map(int, input().split())
# 2개의 수 중에서, 가장 작은 값을 골라 내고, 가장 작은 값을 2로 나눠서 몫을 출력
SASA = min(N, M)
print(SASA//2)