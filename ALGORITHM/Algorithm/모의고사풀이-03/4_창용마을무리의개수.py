import queue
import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-05/1회차/김유영/_창용마을무리의개수.txt")

def dfs(start):
    stack = [start] # 돌아갈 곳 기록
    visited[start] = True # 시작 정점 방문처리

    while stack: # 스택이 빌때까지 반복
        cur = stack.pop() 

        for adj in graph[cur]:
            if not visited[adj]:
                stack.append(adj)
                visited[adj] = True

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range (n+1)]
    visited = [False] * (n+1)
    total = 0

    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    # 무리 한개의 탐색을 마칠때 마다 값 추가 
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            total += 1
            
    print('#{} {}'.format(tc, total))


    