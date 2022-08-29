# https://www.acmicpc.net/problem/11724

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220810/연결 요소의 개수.txt")

# dfs 만들어주기
def dfs(start):
    stack = [start]
    visited[start] = True
    
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
        
n,m = map(int, input().split())   # 정점과 간선의 개수 
graph = [[] for _ in range(n + 1)]  # 인덱스가 1부터 시작해서 +1

# 인접 리스트
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
count = 0

# 노드 하나씩 보면서 덩어리가 나오면 증가! 
for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        count += 1
print(count)
        
