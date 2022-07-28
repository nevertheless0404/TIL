# https://www.acmicpc.net/problem/2789

A = "CAMBRIDGE"
N = list(input())
for i in A:
    for j in range(len(N)):
        if i == N[j]:
            N[j]=""
for i in N:
    print(i, end=" ")