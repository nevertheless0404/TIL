# 합
# n이 주어졌을 때, 1부터 n까지 합을 구함

n = int(input())
total = 0  # 변수에 0을 지정
for i in range(1, n+1): # 1부터 n까지
    total += i

print(total)