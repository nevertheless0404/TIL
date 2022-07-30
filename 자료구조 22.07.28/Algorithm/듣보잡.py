# https://www.acmicpc.net/problem/1764

N, M = list(map(int, input().split()))
D = []
B = []
# N의 크기만큼 듣도못한 사람을 입력
for i in range(N):
    D.append(input())
for i in range(M):
    B.append(input())
answer = list(set(D) & set(B))
print(len(answer))
answer.sort()
for n in answer:
    print(n)
