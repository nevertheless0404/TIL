# https://www.acmicpc.net/problem/1357

X, Y = map(str, input().split())
S = str(int(X[::-1])+ int(Y[::-1]))
print(int(S[::-1]))