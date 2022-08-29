# https://www.acmicpc.net/problem/2606

from functools import total_ordering
import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220810/바이러스.txt")

n = int(input()) # 정점 개수(컴퓨터)
m = int(input()) # 간선 개수(네트워크)
graph =[[]for _ in range(n+1)]  # 인덱스가 1부터 시작 해서 +1
visited = [False] * (n+1)
total = 0
# 인접 리스트 만들기 
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1) # 1번 정점에서 시작 
print(sum(visited)-1)