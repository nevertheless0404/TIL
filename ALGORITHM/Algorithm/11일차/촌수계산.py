# https://www.acmicpc.net/problem/2644

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220810/촌수계산.txt")

n = int(input())
a, b = map(int, input().split())
m = int(input())
# _: 값을 사용하지 않겠다는 의미 
graph = [[] for _ in range(0, n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)

for _ in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)
# 자식노트에 도착하는 경우 부모노드가 갖는 촌수에 +1
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result[i] = result[v] + 1
            dfs(i)

dfs(a)
if result[b] > 0:
    print(result[b])
else:
    print(-1)
