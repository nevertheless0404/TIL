# https://www.acmicpc.net/problem/5576

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220810/콘테스트.txt")

w = []
k = []

# 대학 입력
for _ in range(10):
    w.append(int(input()))

for _ in range(10):
    k.append(int(input()))

# 내림차순으로 정렬
# 득점을 높은 사람을 구해야 하기 때문 
w.sort(reverse=True)
k.sort(reverse=True)

w_score = 0
k_score = 0

for i in range(3):
    w_score += w[i]
    k_score += k[i]

print(w_score, k_score)